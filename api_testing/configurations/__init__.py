try:
    from .domain import Covid19StatisticsConfig
    from .domain import FakeRestAPIConfig
except ImportError as e:
    print(f"import configurations error: {str(e)}")
    from .domain import Covid19StatisticsConfig
    from .domain import FakeRestAPIConfig
