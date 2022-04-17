* Install all packages - pip install -r requirements.txt
* Migration before running server - python3 manage.py migrate
* Load products from fixtures - python3 manage.py loaddata categories + python3 manage.py loaddata products (first categories & then the products)
* Run local server - python3 manage.py runserver