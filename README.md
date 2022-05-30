## Pixel-gallery
## By Oliver Maiyo

### Screenshot of the App
<img src="https://raw.githubusercontent.com/Olliemint/Pixel-gallery/main/static/images/pixels-landing.png">


## Table of Content

+ [Description](#description)
+ [Setup/Installation Requirements](setup&installationrequirements)
+ [How To Access the Site](#howtoaccessthesite)
+ [UserStory](#userstory)
+ [Technology & Tools](#technology&tools)
+ [Reference](#reference)
+ [Known-Bugs](#knownbugs)
+ [Licence](#licence)
+ [Authors Info](#authors-info)

## Description
Django app that display images ,image category and also allow single image view and shows image description. A user can filter images by category or location and copy image link address

## Setup and Installation  
To get the project .......  
  
##### Clone Repository:  

clone from this link https://github.com/Olliemint/Pixel-gallery.git

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


## Access the website
Need the latest browser to be able to View

Follow this link https://pixelstour.herokuapp.com/

It is hosted on heroku

---

## User Stories  
User Can :-

* View different photos that interest them  
* Click a single image to expand it and view the details of that photo  
* view different images categories in a single page 
* Copy image link address and share
* Search images based on category name
* Filter images by category or location
 

---

  
## Technology used  
  
* HTML, CSS, Bootstrap

* Git

* Python, Django Framework

* Heroku 
  
  
## Bugs  
* no known bugs at the moment

### License
MIT License

Copyright (c) 2022 Oliver Maiyo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
  
## Contact Details
oliverkoechrj@gmail.com

@furymint(Twitter)


---
