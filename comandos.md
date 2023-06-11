python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
pip freeze > requirements.txt
pip check -r requirements.txt
py manage.py makemigrations
py manage.py migrate
py manage.py migrate --run-syncdb
py manage.py loaddata .\moodMatch\fixtures\starterdb.yaml
py manage.py loaddata .\moodMatch\fixtures\genres-song.yaml
py manage.py loaddata .\moodMatch\fixtures\songs.yaml
py manage.py createsuperuser
py manage.py runserver
git archive --format=zip --output=moodMatch.zip HEAD
python manage.py collectstatic