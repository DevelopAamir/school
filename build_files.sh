echo "BUILD START"
python --version
pip install requirements.txt
python manage.py collecttatic --noinput --clear

echo "Build Complete"
