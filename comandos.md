python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
pip freeze > requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver