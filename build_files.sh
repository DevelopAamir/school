echo "BUILD START"
python --version
pip install -r requirements.txt
python manage.py collecttatic --noinput --clear

echo "Build Complete"
