# treesandpeople
Polyculture forrest modelling using Python and Django.

## Requirements
* [PostgresSQL 9.3+](https://www.postgresql.org/download/)
* [Python 3.4+](https://www.python.org/downloads/)
* [pipenv](https://docs.pipenv.org/#install-pipenv-today)

## Getting started
This is a standard Django 2 project, using pipenv to manage dependencies.

1. Clone the project with Git: `git clone https://github.com/dsrp/treesandpeople.git`
2. Install project dependencies: `pipenv install` (from project directory)
3. Activate environment: `pipenv shell`
4. Create Postgres user and database:
   ```shell
   $ createuser treesandpeople
   $ createdb -O treesandpeople -E UTF-8 treesandpeople
   ```

   Warning: in production SET A PASSWORD!
5. (Temporarily) create migrations: `treesandpeople/manage.py makemigrations`
6. Populate the database: `treesandpeople/manage.py migrate`
7. Create superuser admin account: `treesandpeople/manage.py createsuperuser`
8. Start development server: `treesandpeople/manage.py runserver`
9. Navigate to `http://127.0.0.1:8000/admin/` and have fun!

## Updating
How to fetch changes from upstream.

1. Fetch changes in code: `git pull`
2. Execute pending migrations: `treesandpeople/manage.py migrate`
