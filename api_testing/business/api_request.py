import json
import logging
import sys
import textwrap

import allure
import requests


class APIRequest:
    def _createLogger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        consoleHandler = logging.StreamHandler(sys.stdout)
        consoleHandler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(message)s'
        )
        consoleHandler.setFormatter(formatter)

        logger.addHandler(consoleHandler)
        return logger

    def __init__(self, waitingTime=None):
        self.waitingTime = waitingTime
        self.requestSession = requests.Session()
        self.logger = self._createLogger()

    @allure.step("[{method}] {url}")
    def _sendRequest(self, method: str, url: str, **kwargs):
        acceptableWaitingTime = kwargs.pop(
            'waiting_time', None) or self.waitingTime
        try:
            response = self.requestSession.request(method, url, **kwargs)
            self._debugPrint(response=response)
            duration = response.elapsed.total_seconds()
            assert duration <= acceptableWaitingTime, (
                f"Response Time > {acceptableWaitingTime}s, Cost: {duration}s")
        except requests.exceptions.RequestException as e:
            response = None
            self.logger.error(
                f"Request Error > url: [{method}] {url}, kwargs: {kwargs}, error: {str(e)}")
        return response

    def _debugPrint(self, response: requests.Response):
        reqBody = response.request.body
        if reqBody:
            reqBody = json.loads(reqBody)

        try:
            res = json.dumps(response.json(), indent=4, ensure_ascii=False)
        except json.JSONDecodeError:
            res = response.text

        def formatHeaders(d): return '\n'.join(
            f'{key}: {val}' for key, val in d.items())

        self.logger.debug(textwrap.dedent('''
                    ---------------- request ----------------
                    {req.method} {req.url}
                    {reqHeader}
                    Request Body :
                    {reqBody}
                    ---------------- response ----------------
                    {resp.status_code} {resp.reason} {resp.url}
                    {respHeader}
                    Duration : {respDuration}
                    Response Context :
                    {respBody}
                    ''').format(
            req=response.request,
            reqBody=json.dumps(reqBody, indent=4, ensure_ascii=False),
            resp=response,
            respBody=res,
            respDuration=response.elapsed.total_seconds(),
            reqHeader=formatHeaders(response.request.headers),
            respHeader=formatHeaders(response.headers),
        ))
