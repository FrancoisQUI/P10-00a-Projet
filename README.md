# P10 Project from OpenClassrooms Python Developper course : 

Create a RESTful API with DjangoRest Frameworks

## Prerequisite :

- python >3.2 + pip
- git
- venv

## Create virtual environment

- Download the files or clone the repo where you want 
```shell
cd {your-desired-path}
git clone git@github.com:FrancoisQUI/P9-01-ProjetV2.git
cd P9-01-ProjetV2
```
- Create and activate your virtual environnement
```shell
python -m venv {your-desired-env-path*}
source {your-desired-env-path*}/activate
```
*the best choice is 'env'
- Install necessary packages
```shell
pip install -r requirements.txt
```


## Create database :
- set DB name in ```softdesk/settings.py```, l82 for debug, l86 for production
```py
DATABASES = {
    'default': {
        "ENGINE": 'django.db.backends.sqlite3',
        "NAME": BASE_DIR / '{dbname_here}.sqlite3',
    }
}
```
don't forget to change ```{dbname_here}``` with what you want

- Migrate with command: 
```shell
python manage.py migrate
```

- Create the Admin Account :
```shell
python manage.py createsuperuser
```
and follow instructions

Don't forget to restart your server.


## Launch the app

- You can switch Debug Mode in ```softdesk/setting.py``` with the `DEBUG` at True or False

This app is in development : if you want to deploy it in production please follow [this guidiline](https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/) ie : don't forget to change and hide the APPKEY.

- Start the server
```shell
python manage.py runserver 
```
- Acces to the application with your favorite Browser : 
[https://127.0.0.1:8000/](https://127.0.0.1:8000/)

