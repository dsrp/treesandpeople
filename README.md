# peopleandtrees
Polyculture forrest modelling using Python and Django.

## Getting started
This is a standard Django 2 project, using pipenv to manage dependencies.

1. Install Python 3
2. Install pipenv: `pip install pipenv`
3. Install project dependencies: `pipenv install`
4. Activate environment: `pipenv shell`
5. (Temporarily) create migrations: `peopleandtrees/manage.py makemigrations`
6. Create development database: `peopleandtrees/manage.py migrate`
7. Create superuser admin account: `peopleandtrees/manage.py createsuperuser`
8. Start development server: `peopleandtrees/manage.py runserver`
9. Navigate to `http://127.0.0.1:8000/admin/` and have fun!
