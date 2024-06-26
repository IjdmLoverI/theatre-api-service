# Theatre-api-service

## Installation using GitHub
````shell
git clone https://github.com/IjdmLoverI/theatre-api-service.git
pip install virtualenv
virtualenv venv
source venv/Scripts/activate
pip install -r requirements.txt
set DB_HOST=<your db hostname>
set DB_NAME=<your db name>
set DB_USER=<your db username>
set DB_PASSWORD=<your db user password>
set SECRET_KEY=<your secret key>
python manage.py migrate
python manage.py runserver
````

# Run with docker
````shell
docker-compose build
docker-compose up
````

# Features
- JWT authentication
- Admin panel /admin/
- Documentation is located at /api/schema/swagger-ui/
- Managing reservations and tickets
- Creating plays with genres, actors
- Creating theatre hals
- Adding performances
- Filtering plays and performances

# Demo
![Endpoints](prev_imgs/img.png)

![Endpoints](prev_imgs/img_1.png)
