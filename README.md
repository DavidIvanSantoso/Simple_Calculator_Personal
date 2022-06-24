# Simple_Calculator_Personal

This is a simple calculator service that gives you a prime number by index from user and prime palindrome number by index.
<br>
I use Django for this project
<br>
Step for setup the django project:
<br>
1. pip install celery
2. pip install django
3. To create a project you need to run this command (admin-django startproject <projectname>)
4. For running the project you need to run thins command first for django localhost (python manage.py migrate)
5. And then continue with this command (python manage.py runserver)
6. If you want to run django project and test it, you can always use python manage.py runserver
7. Open localhost:8000 to test it.
8. For this project first function, write localhost:8000/prime/<int:index> (<int:index> you can insert any number that you want to check what prime number in that index that you put)
9. For the second function write, write localhost:8000/primepalindrome/<int:index>  (<int:index> you can insert any number that you want to check what prime palindrome number in that index that you put)
