# Instagram-Clone

>[Ahmed Mohamed](https://github.com/Ahmed-moringa)  
  
# Description  
This is a clone of the popular application Instagram where people share their images and videos for other users to view. 
Users can sign up, login, view and post photos, search and follow other users.
##  Live Link  
 Click [View Site](https://instagram177.herokuapp.com/account/login/?next=/)  to visit the site
  
## Screenshots 
###### Home page
 
[![instagra.png](https://i.postimg.cc/8sQnXwwR/instagra.png)](https://postimg.cc/kRscBQ0G)
 

## User Story  
  
* Sign in to the application to start using.  
* Upload a pictures to the application. 
* Search for different users using their usernames.  
* See your profile with all your pictures.  
* Follow other users and see their pictures on my timeline.  
  
  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/Ahmed-moringa/Instagram-clone.git 
```
##### Navigate into the folder 
 ```bash 
cd Instagram-clone
```
##### Install and activate Virtual Environment
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make Migrations  
 ```bash 
python manage.py makemigrations Insta
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python](https://www.python.org/)  
* [Django](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [ahmed.mohamed@student.moringaschool.com]  
  
## License 

* Copyright (c) 2022 **Ahmed Mohamed**