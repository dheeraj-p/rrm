# Room Rate Management

This project was built on **python3.12**

Swagger UI is available on http://localhost:8000/swagger


### Local Setup Instructions

- Create a virtual environment
- Install dependencies from requirements.txt 
- Run MySQL local server on port 3306 (With following) Or update the DB configurations in `room_rate_management/settings.py`
  - Default Database name is `rrm`
  - Default username is `root`
  - Default password is `root`
- Run database migrations using `python manage.py makemigrations && python manage.py migrate`
- Run Development server `python manage.py runserver`