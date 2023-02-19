echo "BUILD START"
python --version
python -m pip install requirements.txt
python manage.py collecttatic --noinput --clear

echo "Build Complete"
