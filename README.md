<a href="https://www.codacy.com/manual/sendador/Django-Human-Log?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sendador/Django-Human-Log&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/7f38ad72c303423890ce8e17f655a9ec"/></a>
[![Build Status](https://travis-ci.com/sendador/Django-Human-Log.svg?branch=master)](https://travis-ci.com/sendador/Django-Human-Log)

# Django Blog:

Blog is just only log for humans isn't?
This is easy to use django blog. Every admin movement is on the django admin panel.

# Technologies:

- Python
- Django
- Unit tests on models, urls, views
- Coverage and codecov to improve test across the app
- Django-environ for environmental variables
- Codacy for automate code reviews and monitors code quality
- Travis CI for continuous integration service used to build and test 
- TinyMCE for convenient post writing
# Docker intallation:
Just clone repo
<pre>git clone https://github.com/sendador/Django-Human-Log.git </pre>
and then use docker-composer
<pre>docker-compose up</pre>
Your app will be on:
<pre>localhost:8000</pre>
# Manual Installation:

You can get repository from git by:
<pre>git clone https://github.com/sendador/Django-Human-Log.git </pre>

It's good to use code in virtual environment. For that you can use virtualenv:

<pre>pip install virtualenv</pre>
Then create your virtualenv
<pre>virtualenv venv</pre>

Next activate virtual environment.<Br>
For Windows powershell
<pre>*your venv dir*\Scripts\activate.ps1</pre>
or windows command
<pre>*your venv dir*\Scripts\activate.bat</pre>

and install other dependency

<pre>pip install -r requirements.txt</pre>
# Usage
Next you have to migrate your new database:

<pre>python manage.py makemigrations</pre>
and then:
<pre>python manage.py migrate</pre>

And then create superuser for admin purposes:

<pre>python manage.py createsuperuser</pre>

Finally you can run for the first time your site:

<pre>python manage.py runserver</pre>

You can login to your admin account through:

<pre>http://127.0.0.1:8000/admin</pre>

And then add some new post.





