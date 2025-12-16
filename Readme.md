
# Inventory Management (Django)

Simple Django-based inventory management project for demonstration and development.

## Contents
- `invProject/` — Django project settings and URL routing
- `authApp/` — authentication-related models and views
- `invApp/` — inventory models, forms, and views
- `usersApp/` — user-related pieces

## Quick Setup
1. Create and activate a virtual environment (pipenv or venv).
2. Install dependencies: `pipenv install` or `pip install -r requirements.txt`.
3. Apply migrations: `python manage.py migrate`.
4. Create a superuser: `python manage.py createsuperuser`.
5. Run the dev server: `python manage.py runserver`.

## Notes
- Database: `db.sqlite3` (default, in repo root)
- Tests: each app has `tests.py` — run `python manage.py test`.

## Contributing
Open an issue or submit a PR with clear changes and tests.

## License
MIT — see project root for license details.

