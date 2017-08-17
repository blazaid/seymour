# Seymour

A Django template with some preconfigured stuff to bootstrap microservices
based on Django and Django REST framework.

## Creating a project based on this template

You can clone the project (as I've been doing until now) or you can start a new
project using the `--template` param (thanks to
[@kasappeal](https://github.com/kasappeal)). I'll stick to this last one.

1. Start a new project with this template

    ```
    $ django-admin.py startproject \
      --template=https://github.com/blazaid/seymour/archive/master.zip \
      <PROJECT_NAME>
    ```

    Be careful to replace the `<PROJECT_NAME>` param with the name of your 
    current project.

2. Install the dependencies
    
    Enable your virtual environment and install them via the `requirements.txt` 
    file.
    
    ```
    $ pip install -r requirements.txt
    ```

3. That's all

    Yes. Nothing more to do here. Well, maybe a barrel roll.

## Contents of the package

Let's assume the project created is `my_service`. After the `startproject` 
command the project structure ends as follows:

```
my_service
│   LICENSE.txt
│   README.md
│   requirements.txt    
│
└───project
    │   manage.py
    │
    └───api
    │   │   admin.py
    │   │   api.py
    │   │   apps.py
    │   │   models.py
    │   │   serializers.py
    │   │   tests.py
    │   │   urls.py
    │   │   views.py
    │   │
    └───config
        │   urls.py
        │   wsgi.py
        │   settings.py
```

The rest of the section explains this structure contents.

### Root layout

| File / directory | Explanation |
|------------------|-------------|
| `./LICENSE.txt` | The description of the license. |
| `./README.md` | This file. |
| `./requirements.txt` | The main requirements (to install via pip). |
| `./project/` | The django project itself. |

By maintaining the django project in an inner directory, we can maintain 
other files and directories (e.g. the `requirements.txt`file, vm 
descriptions with dockerfiles, depoy scripts, documentations, etc.) outside 
the main project in django.

#### Django project layout (`project` directory)

The project will be stored inside the `project` directory. It's name can be 
replaced without any problem.

| File / directory | Explanation |
|------------------|-------------|
| `./manage.py` | The file for launching the commands of this django project. |
| `./api/` | A django application to store the logic of the micro service. |
| `./config/` | The configuration of the django project. |

It's possible to have more than one application inside the project (after all,
it's a normal django project), but as it represents a micro-service, it's
preferable to maintain it as small as possible so I think that one sole 
application is enough in the vast majority of the cases.

##### Django application layout (`api` directory)

The `api` directory holds all the logic of the service. It's a normal django
application (so there is no need to explain the usual files) with three more 
files.

| File / directory | Explanation |
|------------------|-------------|
| `./api.py` | Contain all the sources for the endpoints of the service. |
| `./serializers.py` | Contains all the serializers of Django Rest Framework. |
| `./urls.py` | Specifies the urls inside the context of the API. |

All the endpoints URL's will be deployed under the /api/ context 
(we'll see it later in `config/urls.py`) 

##### Django configuration layout (`config` directory)

It holds the configuration of the django project. The main differences with 
a normal django project are the name (is named config instead) and that the 
key variables to configure are specified as environment variables.

The user can replace the calls to `os.environ` by the variables to configure or
create the variables in the environment. The configurable variables shown in
 the next table.

| Variable | Description | Mandatory | Defaults |
|----------|-------------| --------- | -------- |
| PROJECT_SECRET_KEY | The secret key of the project | Yes | None |
| PROJECT_DEBUG | If the debug mode is enabled (True/False) | No | False |
| PROJECT_ALLOWED_HOSTS | A list of allowed hosts (',' sep.) | No | 127.0.0.1 |
| PROJECT_DB_ENGINE | The engine string of the database driver | Yes | None |
| PROJECT_DB_NAME | The database name | Yes | None |
| PROJECT_DB_USER | The user allowed to access to the database | No | '' |
| PROJECT_DB_PASSWORD | The users password | No | '' |

## Python versions

It's expected to work with any 3.3 or higher version of django. Lower 
versions could work to, but will be necessary to add an `__init__.py` file in 
the sources directories in order to be recognized as packages by django.

## License

This project is licensed under the terms of the MIT license. More information
is available in [license file](LICENSE.txt) and in
https://tldrlegal.com/license/mit-license.

## About the name

Seymour Asses is the Philip J. Fry dog who was waiting for its owner since he
got frozen. However, in a latter chapter, a Fry's clone travels in time and
supersedes Fry in the past so we hope Seymour had a happy life.

The reason to choose this name is because I like that dog. That's all :D.

