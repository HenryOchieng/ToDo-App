# ToDoApp
> A web-based task management application

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#features)
* [Setup](#setup)

## General info
This is a simple django-based application that helps users effectively manage their daily tasks.
	
## Technologies
The project was built using:
* Python version 3.8.7
* Django verion 3.1.6
* Bootstrap version 4
* HTML
* CSS

## Features
These are the features of this project
* User can add task they want to perform
* User can delete a single task 
* User can delete entire list of tasks

## Setup

1. Git Clone the project with: ```git clone https://github.com/HenryOchieng/ToDo-App.git```.

2. Move to the base directory: ```cd ToDo-App```

3. Create a new python enveronment with: ```python -m venv env```.

4. Activate enveronment with: ```env\Scripts\activate``` on windows, or ```source env/bin/activate``` on Mac and Linux.

5. Install required dependences with: ```pip install -r requirements.txt```.

6. Make migrations with: ```python manage.py makemigrations``` and then ```python manage.py migrate```.

7. Run app localy with: ```python manage.py runserver```.


