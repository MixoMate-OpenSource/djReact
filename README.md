# Django + React Starter Template
Open-source Django Starter coded with react.

[![version](https://img.shields.io/github/package-json/v/GoCommix-OpenSource/Dj-react-starter-template?filename=frontend%2Fpackage.json)]()
[![version](https://img.shields.io/github/pipenv/locked/dependency-version/GoCommix-OpenSource/Dj-react-starter-template/django)]()
[![version](https://img.shields.io/github/pipenv/locked/python-version/GoCommix-OpenSource/Dj-react-starter-template)]()
[![version](https://img.shields.io/github/package-json/dependency-version/GoCommix-OpenSource/Dj-react-starter-template/react?filename=frontend%2Fpackage.json)]()

Hi there !!, this repository will help you crete production level `django + react` project, by using a single command.

## Using the template to create a new project

make sure that django is already installed in your system as we need django-admin command to create a project using this template.


First of all you need to run the command below:

```bash
django-admin startproject --template https://github.com/GoCommix-OpenSource/Dj-react-starter-template/archive/refs/heads/feature/basic.zip hello_world D:\hello_world_project
```
> Note : I have used  `D:\hello_world_project` as parent folder of the project and `hello_world` as the project name but you can use any destination folder and project name as per your need.

Now we have our `django+react` project generated using our `basic` template  at `D:\hello_world_project`

```bash
.\hello_world_project #project parent directory
│
├── hello_world\  # django main app
│   ├── __init__.py
│   ├── asgi.py
│   ├── common_settings.py # default  setting file connected with .env file
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── error_handler\
│   │
│   ├── migrations\
│   │   └── __init__.py
│   │
│   ├── templates\
│   │   └── error_page.html
│   │
│   ├── __init__.py
│   ├── apps.py
│   ├── tests.py
│   └── views.py
│
├── frontend\  # react app lies in this folder
│   │
│   │
│   ├── src\
│   │   │
│   │   ├── assets\
│   │   │   └── react.svg
│   │   │
│   │   ├── pages\
│   │   │   │
│   │   │   └── home\
│   │   │       └── index.jsx
│   │   │
│   │   │
│   │   ├── App.css
│   │   ├── App.tsx
│   │   ├── constants.tsx
│   │   ├── index.css
│   │   ├── main.tsx
│   │   └── vite-env.d.ts
│   │
│   ├── index.html
│   ├── package.json
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   ├── vite.config.ts
│   ├── yarn-error.log
│   └── yarn.lock
│
├── .env      # example .env file already in use, make sure to add this in your .gitignore to hide sensitive information.
├── .gitignore
├── Pipfile
├── Pipfile.lock
├── README.md
└── manage.py
```

further you can use any feature branch to create different templates using the syntax below:


```html
django-admin startproject --template https://github.com/GoCommix-OpenSource/Dj-react-starter-template/archive/refs/heads/feature/<branch-name>.zip <app-name> <parent-folder>
```

## Install dependencies for django and react

you may required pipenv and yarn/npm for this:
```bash
cd D:\hello_world_project
pip install pipenv
pipenv install

cd frontend
yarn
```

## Serving React app on Django

It's very easy to serve your react app with django for this you just need to run react build on `watch` while your django app is running. For that follow the process below.

. Open a terminal to run django app
```bash
pipenv shell
py manage.py runserver
```

. Open a terminal in `frontend` folder to run  react app using command:
```bash
yarn dev
```

now go to http://localhost:8000 to see you django+React app running.


For full documentation go to [comming soon]()
