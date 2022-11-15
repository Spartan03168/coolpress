rm "*/migrations/*.py" -Exclude "__init__.py"
rm "*/migrations/*.pyc"
rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb