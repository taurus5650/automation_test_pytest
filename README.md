> # Intro
### **Purpose**
* For testing, which using
  * Pytest framework
  * Jenkins
  * Allure report
  * Docker
* Support testing
  * http api testing
  * `ToDo` web selenium testing

### **Directory Structure**
```bash
git ls-tree -r --name-only HEAD | tree --fromfile

.
├── .gitignore
├── Dockerfile
├── README.md
├── __init__.py
├── api_testing
│   ├── __init__.py
│   ├── business
│   │   ├── __init__.py
│   │   ├── api_request.py
│   │   ├── books
│   │   │   └── api
│   │   │       ├── __init__.py
│   │   │       └── books_api.py
│   │   └── users
│   │       └── api
│   │           ├── __init__.py
│   │           └── users_api.py
│   ├── configurations
│   │   ├── __init__.py
│   │   └── domain.py
│   ├── conftest.py
│   └── test_suites
│       ├── books
│       │   ├── __init__.py
│       │   └── test_get_books_id.py
│       └── users
│           ├── __init__.py
│           ├── test_get_users.py
│           └── test_post_user.py
├── deployment
│   ├── Jenkinsfile
│   └── job_configurations.json
└── requirements.txt

```

--- --- ---

> # Step-by-step

## **Docker**
### Build up Jenkins Docker
##### Ref : [How to Run Jenkins Container as Systemd Service with Docker](https://www.linuxtechi.com/run-jenkins-docker-container-systemd/)

* Build a Jenkins run in Docker
  * `--name jenkins` : Container naming
  * `-p 8080:8080` : Container 8080 port mapping to localhost 8080 port, which for jenkins administrator login.
  * `-p 50000:50000` Container 50000 port mapping to localhost 50000 port, which for jenkins slave node's JNLP (Java Web Start) port.
  * `-v ~/jenkins_home:/var/jenkins_home` : Build up docker volume. Container /var/jenkins_home mapping to localhost ~/jenkins_home.
  * `-v /var/run/docker.sock:/var/run/docker.sock` : Let containers can use docker daemon.
```commandline
docker run --name jenkins -p 8080:8080 -p 50000:50000 -v ~/jenkins_home:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins:lts
```

* Started the container and command
```commandline
- apt-get update
- apt-get install -y wget
- wget https://github.com/allure-framework/allure2/releases/download/2.14.0/allure-2.14.0.zip
- unzip allure-2.14.0.zip
- export PATH=$PATH:/path/to/allure-2.14.0/bin
```

* _If docker cli encountering no permission_
```commandline
docker exec -u 0 -it {#CONTAINER_ID} /bin/bash
```

## **Jenkins**
### Unlock Jenkins and build up
* Way to http://localhost:8080/ 
* Unlock the Jenkins with password.
The password form **container's logs** when u started the container.
* Install suggested plugins

##### Ref : [How to Run Jenkins Container as Systemd Service with Docker](https://www.linuxtechi.com/run-jenkins-docker-container-systemd/)

------- ------- ------- _Demarcations_ ------ ------ ------


## **Jenkins**

### Build pipeline
* In this case, the job will separate by services. 
Thus, We may create the pipeline by services.
  * API : Users
  * API : Books
```commandline
│   └── test_suites
│       ├── books
│       │   ├── __init__.py
│       │   └── test_get_books_id.py
│       └── users
│           ├── __init__.py
│           ├── test_get_users.py
│           └── test_post_user.py
```
* Select new items build a new job
![jenkins_new_item.png](git_readme%2Fjenkins_new_item.png)
* Give a job naming and select pipeline
![jenkins_choose_pipeline.png](git_readme%2Fjenkins_choose_pipeline.png)
* Do the config
  * Repository URL : Git repo
  * Credentials : Ref [How To Add Git Credentials In Jenkins](https://www.cybrosys.com/blog/how-to-add-git-credentials-in-jenkins)
  * Branches to build : */master
  * Script Path : **deployment/Jenkinsfile**
![jenkins_pipeline_config.png](git_readme%2Fjenkins_pipeline_config.png)

### Okieee, then run the job
* Build parameters
![jenkins_job_builds_params.png](git_readme%2Fjenkins_job_builds_params.png)
* Input parameters (optional, if didn't input then run as default)
![job_run_build.png](git_readme%2Fjob_run_build.png)
* Job complete
![jenkins_job_complete.png](git_readme%2Fjenkins_job_complete.png)
* May way to allure report to check the result =)
![allure_report.png](git_readme%2Fallure_report.png)