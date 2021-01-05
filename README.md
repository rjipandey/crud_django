# crud_django

Install Python by adding PYTHON to PATH.
install virtualenv (pip install virtualenv)
Create Virtual Env ( python -m venv envname)
Activate virtual environment. (Path'envname'\scripts\activate)
install requirements (pip install -r requirements.txt)
Open MySQL.
Create User as given in settings.py of project.  (DataBase Connection is commented for MySQL Connection)
Create database as given in settings.py of project. (To Use MySQL Database uncomment the DATABASES part for mySQL in settings.py and comment the SQLite3 Connections.
create migrations (python manage.py makemigrations)
execute migrations ( python manage.py migrate)
start server (python manage.py runserver)
visit to http://127.0.0.1:8000/emp/
Perform Crud Operations.
Done
