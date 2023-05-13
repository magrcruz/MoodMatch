venv\Scripts\activate.bat
pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py migrate --run-syncdb
py manage.py createsuperuser
py manage.py runserver