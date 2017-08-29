## Bucket List App
This is Django App that creates bucket lists of stuff that we would like to do in the future.

**Specs**
1. App can create a bucketlist
2. App can edit a bucketlist
3. App can delete a bucketlist
4. User owns a bucketlist
5. User must be authenticated

**Tech Used**
1. Python 
2. Django
3. Django Rest Framework

**Setup and Installation**
```
$ git clone https://github.com/ngenovictor/bucketlist.git
$ cd bucketlist
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip install < requirements.txt
$ cd djangorest
$ python3 manage.py makemigrations && python3 manage.py migrate
$ python3 manage.py runserver
```
> open [http://localhost:8000/bucketlists/](http://localhost:8000/bucketlists/)

See the [Api Endpoints Documentation](Documentation.md)

**Licence and copyright**
Ngeno Victor, Moringa School
Licensed under [MIT Licence](license)