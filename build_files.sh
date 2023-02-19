echo "BUILD START"
python --version
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic

echo "Build Complete"
