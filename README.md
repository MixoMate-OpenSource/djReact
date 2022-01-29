# Django + React app using webpack
***This is an starter project for react frontend and django backend application***

In project root dir, there are two folders frontend and backend.
The frontend folder is actually a django app that is configured to serve react frontend with django.
# Commands that you can use are

## install dependencies

### 1. pip install
#### Note: Don't forget to activate your virtual environment(if you are using any)
install all the deoendencies for django project
```
pip install -r requirements.txt
```


### 2. yarn install
install all the dependendencies for your react app 
```
cd frontend && yarn install
```

## Other Usefull commands
### 1. yarn start
this will start (react)frontend server ***(only for frontend development)***
```
cd frontend
yarn start
```
your application must be running at http://localhost:3000/

### 2. yarn dev with python manage.py runserver
this command will watch the changes and build react-frontend for develpoment with the help of webpack, as you make changes in your frontend code. The build is directly served by django seamlessly, without putting any extra effort.

```
cd frontend
yarn dev
```
and in another terminal
***Note:*** if you are running it first time you may want to run ```python manage.py collectstatic``` command
```
cd ..
python manage.py runserver
```



and the application must be running as http://localhost:8000/

### 3. yarn build
this command will help you create new optimized build.
```
cd frontend
yarn build
```
this build then will be used by Django as we've seen in above example.

### some other command that are usefull are 
these command are react default commands that also works here
### yarn test
### yarn eject
