echo "BUILD START"
python3.10.9 -m pip install requirements.txt
python3.10.9 manage.py collecttatic --noinput --clear

echo "Build Complete"