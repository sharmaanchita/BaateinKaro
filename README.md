# BaateinKro 
A real time chat app.

It contains the following features:
1. Public chat room for all loged in users
2. Private chat with single user
3. User authentication and verification - Sign In, Sign Out
4. User settings - Logout, Edit Profile, Change Email, Delete Profile, Profile view 

## Techstack
The following techstack was used to develop this project.
* Django
* Python
* WebSocket
* Channels
* HTMX
* Daphne

## Working and Installation
The app provides a real-time chat room for all logged in users using websocket, htmx. Use of Daphne server for ASGI configurations.
Further trying to implement group chat and use redis for faster rendering. 

Run the following commands

Setup virtualvenv(best to use python 3.10.7)
```
python3.10 -m venv venv
cd venv/Sripts/activate
```
Install all requirements
```
pip install -r requirements.txt
```
for Daphne - ASGI configurations and settings.py file is altered accordin to daphne server 
```
pip install -U channels[Daphne]
```
Setup models
```
python manage.py makemigrations
python manage.py migrate
```
Run server
```
python manage.py runserver
```



