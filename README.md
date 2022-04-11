# FinalProject
# Final Project for MAD-2.
````
This is Flash Card App. It has mutiple language support.
WE HAVE DECK MANAGEMENT, LOGIN, DECK REVIEW FACILITY.
IT USES JAVASCRIPT.
WE ALSO APP API IMPLEMENTATION
We have use Vue JS Version 2 and Vuex.
````

This is my Final Project for MODERN APPLICATION DEVELOPMENT  -  2 course

# THIS PROJECT USES -
```
1.	Flask (A Python Framework for designing web applications.) 
2.	Flask Security Too (To prevent apps from abuse) 
3.	Flask Login (For Login Implementation) 
4.	Flask SQLAlchemy (For creating the model of the Decks, Cards etc.) 
5.	Flask RestFull (For implementing API ’s in REST Architecture) 
6.	Jinja2 (For designing the Templates) 
7.	JavaScript (Consuming API and DOM MANIPULATION) 
8.	CSS (For Making Web pages Look Good) 
9.	Vue JS (Front-End Management) 
10.	Vuex (Vue JS State Management) 
11.	Bootstrap (Aesthetics) 
12.	HTML [Web-pages Design] 
13.	SQLITE (For the Database) 
14.	Redis (Message Broker)
15.	Celery (Python Framework for Task queue implementation)
16.	Flask Caching (Adds caching support to your Flask application.)

```

THIS IS DESIGNED ON PYTHON 3.7.3

METHOD TO RUN-
```
CLONE THIS REPO
pip install -r requirements.txt
python3 main.py
```

# For Async Jobs kindly ensure you have - 

```
Redis installed and configured.
Celery installed and configurred.
```
Kindly run celery workers from -

````
celery -A celeryConfig workers --loginfo=info
````

It has both workers and beats configured.

# THE APP CREATES DATABASE FOR EVERY RUN. KINDLY DELETE PREVIOUS DATABASE.SQLITE3 FILE BEFORE ANY RUN.

```
# THE TEST FOLDER CONTAINS TEST.
TO RUN TEST , EXAMPLE DECKS-
```
cd tests
python3 test_decks.py
```

PLEASE FEEL FREE TO CONNECT ON 21F1006475@STUDENT.ONLINEDEGREE.IITM.AC.IN