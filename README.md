# arbrawf

## setup
<pre>
$ python3 -m venv venv
$ source venv/bin/activate
</pre>

## use
<pre>
$ pip install pytest
$ pip install django==1.11.7
</pre>

## report
<pre>
$ pytest --junit-xml=test_result.xml
</pre>

## create Django project
<pre>
$ django-admin startproject apps
$ la -R
.:
合計 12K
drwxr-xr-x 3 koge koge 4.0K  7月  6 23:29 apps

./apps:
合計 16K
drwxr-xr-x 2 koge koge 4.0K  7月  6 23:29 apps
-rwxr-xr-x 1 koge koge  802  7月  6 23:29 manage.py

./apps/apps:
合計 20K
-rw-r--r-- 1 koge koge    0  7月  6 23:29 __init__.py
-rw-r--r-- 1 koge koge 3.1K  7月  6 23:29 settings.py
-rw-r--r-- 1 koge koge  761  7月  6 23:29 urls.py
-rw-r--r-- 1 koge koge  386  7月  6 23:29 wsgi.py
$ 
$ cd apps/
$ python manage.py startapp menu
$ la -R menu/
menu/:
合計 32K
-rw-r--r-- 1 koge koge    0  7月  6 23:31 __init__.py
-rw-r--r-- 1 koge koge   63  7月  6 23:31 admin.py
-rw-r--r-- 1 koge koge   83  7月  6 23:31 apps.py
drwxr-xr-x 2 koge koge 4.0K  7月  6 23:31 migrations
-rw-r--r-- 1 koge koge   57  7月  6 23:31 models.py
-rw-r--r-- 1 koge koge   60  7月  6 23:31 tests.py
-rw-r--r-- 1 koge koge   63  7月  6 23:31 views.py

menu/migrations:
合計 8.0K
-rw-r--r-- 1 koge koge    0  7月  6 23:31 __init__.py
</pre>

### create Migration file
<pre>
$ python manage.py makemigrations
</pre>
