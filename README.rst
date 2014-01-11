What is Heroku
-------------
Heroku is a service that lets you deploy your web application by doing a ``git push`` command. You pay heroku to take care of security and deployment. It allows you to focus your time and energy on developing apps. Heroku's competitors are Engine Yard, Gondor, Cloud9, Nitrous.IO, Google App Engine and many more.

How To Run
==========

Step 1. Install cookiecutter
``   
$ pip install cookiecutter      
``
Step 2. Run cookiecutter 
``
$ cookiecutter git@github.com/pebreo/cookiecutter-django-heroku-basic
``
Step 3. Install requirements
``
$ pip install -r requirements.txt
```

Step 4. Syncdb
```
$ cd myrepo
$ python manage.py syncdb
```
Step 5. Runserver
```    
$ python manage.py runserver
```
Step 6. Run Django admin
```
Goto: localhost:8000/admin
```

Deploying a Django site via Heroku
--------------------------------
To deploy via Heroku, you basically have to do 3 things:  install Heroku, and setup your Django project, and deploy using a ``git push heroku master``.

Here are the steps in detail:

.. code:: bash

    # Setup Heroku
    gem install heroku
    heroku keys:add mykey.pub
    heroku keys
    pip install django-toolbelt
    
    # Setup project
    cd myproj
    git init
    heroku create
    heroku config:set SECRET_KEY=myscretekeybaz
    git add .
    git commit -m "initial commit"
    
    # Deploy project
    git push -u heroku master
    heroku run python manage.py syncdb
    heroku run python manage.py shell 
    
    # Useful commands
    heroku ps:scale web=1
    heroku ps
    heroku open
    heroku config
    heroku logs

    # Manually add Heroku repo
    git remote add heroku git@heroku.com:salty-shelf-8861.git 
    from django.conf import settings; settings.configure()

**Shortcut for Deployment**
I'v added a Makefile so that you can just type:

.. code:: bash

    $ make build
    $ make deploy


A basic requirements.txt file should look like this:

.. code:: bash

    Django==1.6
    South==0.8.1
    argparse==1.2.1
    dj-database-url==0.2.2
    #djangorestframework==2.3.7
    gunicorn==18.0
    psycopg2==2.5.1
    static==0.4
    requests==1.2.3
    wsgiref==0.1.2

**Links**

Here is the `Getting Started with Django on Heroku <https://devcenter.heroku.com/articles/getting-started-with-django>`_ page.





