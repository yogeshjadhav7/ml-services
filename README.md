# ml-services

### Description
----
This Python project uses Django FrameWork and is used as REST Machine Learning microservice by my ML projects. This service is live at http://ai.yogeshjadhav.website/.

### Prerequisites 
---
> Install and setup **intellecto** project (https://github.com/yogeshjadhav7/intellecto)
```sh
Go through the installation steps specified in the README of intellecto project. Also, it is recommended to set up pyenv and virtualenv to create a separte python environment.
```

### Installation
----
> Clone the repository.
``` sh
git clone https://github.com/yogeshjadhav7/ml-services.git
```

> Go to the root directory of the project.
``` sh
cd ml-services/
```

> Install the requirements.
```sh
pip install -r requirements.txt 
```

> Apply the migrations initially.
``` sh
python manage.py migrate
```

> Test the installation by running the service.
``` sh
python manage.py runserver
```

### Production Deployment
---
> Go to the directory.
``` sh
cd path-to-root-dir-of-project
```

> We would be using port 8000 for this service. Firstly, check whether any process is using that port. Kill the process if it is using 8000 port. This will also help in redeployment of this service by terminating the already running instance on the same port.
``` sh
lsof -n -i :8000 | grep LISTEN | awk '{ print $2 }' | uniq | xargs kill -9
```

> We would be using nohup to run the service in background. Delete the nohup.out file which is created by previously running instance of the service.
```sh
rm nohup.out
```

> Finally, start the Django service by commanding gunicorn to load the project's WSGI module. We would be using nohup to keep the service running in background.
```sh
nohup gunicorn ml_services.wsgi:application --bind 127.0.0.1:8000 &
```

> OR you could use the already created shell script **prod.sh** to deploy with your correcsponding changes.
``` sh 
sh prod.sh
```


