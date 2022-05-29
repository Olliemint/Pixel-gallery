# Pixel-gallery
Django app that display images ,image category and also allow single image view and shows image description. A user can filter images by category or location and copy image link address

## User Stories  
User Can :-

* View different photos that interest them  
* Click a single image to expand it and view the details of that photo  
* view different images categories in a single page 
 

---
## Access the website
Need the latest browser to be able to View

Follow this link https://cornygallery.herokuapp.com/

It is hosted on heroku

---

## Setup and Installation  
To get the project .......  
  
##### Clone Repository:  

clone from this link https://github.com/Olliemint/Django-photogallery.git

##### Install and activate Virtual Enviroment envgallery  
 ```bash 
cd project directory  && python3 -m venv penv && source envgallery/bin/activate 
```  
##### Install Dependencies  
 ```bash 
 pip3 install -r requirements.txt 
```  
##### Setup Database  
  SetUp Database User,Password, Host then following Command  
 ```bash 
python manage.py makemigrations photo 
 ``` 
 Now Migrate  
 ```bash 
 python3 manage.py migrate 
```
##### Run Application  
 ```bash 
 python3 manage.py runserver
```
##### Test Application  
 ```bash 
 python3 manage.py test photo
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* HTML, CSS, Bootstrap

* Git

* Python, Django Framework

* Heroku 
  
  
## Bugs  
* no known bugs at the moment
  
## Contact Details
oliverkoechrj@gmail.com

@furymint(Twitter)


---

### License
This Project is under the [MIT](LICENSE) license
