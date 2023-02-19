echo "BUILD START"
python --version
pip install -r requirements.txt
python manage.py collectstatic

echo "Build Complete"
