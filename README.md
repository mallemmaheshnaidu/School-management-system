# School Portal

This is a Django project providing a simple school management frontend and backend.

Features:
- Students, ClassRoom, Subjects, Books, Attendance, Marks models
- Admin registration for easy data entry
- Professional-looking frontend (Bootstrap) to list students and view details

Quick start (Windows PowerShell):

```powershell
# activate virtualenv
& .\env\Scripts\Activate.ps1
# install Django if needed
pip install django
# make migrations
python manage.py makemigrations
python manage.py migrate
# create admin user
python manage.py createsuperuser
# run server
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to view students list. Use the admin at /admin to add ClassRoom, Subject, Book, Student, Attendance and Marks.
