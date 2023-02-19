echo "BUILD START"
python --version
pip install asgiref
pip install Django
pip install django-ckeditor
pip install django-crispy-forms
pip install django-js-asset
pip install gunicorn
pip install Pillow
pip install sqlparse
python manage.py collectstatic

echo "Build Complete"
