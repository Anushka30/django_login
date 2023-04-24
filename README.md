## Create a REST API for a login/signup page using Django and Mysql. Here are the steps:

### Install required packages:

```sh
pip install django djangorestframework mysqlclient
```

### Create a new Django project:

`django-admin startproject myproject`

### Create a new Django app within the project:

```sh
cd myproject
python manage.py startapp signup
```

### In the settings.py file, adding database connection details like below:

```sh
{
'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

#### Migrate the models to the MySQL database using the command `python manage.py makemigrations` and `python manage.py migrate`.

#### Run Django server using the command `python manage.py runserver` and test the API using a REST client like Postman.
