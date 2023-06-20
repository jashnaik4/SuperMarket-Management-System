# SuperMarket-Management-System
Instructions for running the project


#### Disclaimer: All the instructions are specified for macOS. And it is assumed that you have installed python3 and django
1. Install ‘mysqlclient’ using the pip command in the terminal.
   * ```pip install mysqlclient```

2. Linking an SQL database
   * create a mysql server and run ```Database_Initialization.sql```  query file inside this.

   * update settings.py with your username and password. The code is somewhat like this:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'supermarket',
            'USER': 'YOUR USERNAME GOES HERE',
            'PASSWORD': 'YOUR DB PASSWORD GOES HERE',
            'HOST': '127.0.0.1',
            'PORT': '3306',
            'OPTIONS': {'init_command':"SET sql_mode='STRICT_TRANS_TABLES'"}
        }
    }
    ```
3. Now install Django and run the server as below
   * change to the directory containing the code
     * ```cd <folder_name>```
   * install django in the current directory
     * ```pip install Django==2.x.x```
   * now migrate the database of django using command line
     1. ```python manage.py makemigrations```
     2. ```python manage.py migrate```
   * start your project
     * ```django-admin.py startproject SuperMarket_System```
   * Run your project
     * ```python manage.py runserver```

To run on browser, click on the link http://127.0.0.1:8000 .
