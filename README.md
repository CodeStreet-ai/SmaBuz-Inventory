# SMABUZ

Inventory management systems for small businesses.

## Development
---
### 1. Clone the git repo:
```shell
git clone git@github.com:CodeStreet-ai/SmaBuz-Inventory.git
```
### 2. Change directory to SmaBuz-Inventory:
```shell
cd SmaBuz-Inventory
```
### 3. Create your branch:
Name your branch based on the feature you are working on. For example, Writing ReadMe branch would be called `feature/write_readme`:
```shell
git checkout -b <your branch name>
```
### 4. Activate Virtual Environment:
```shell
python3 -m venv <your env name>
. env/bin/activate
```

### 5. Install Dependencies:
```shell
pip install -r "requirements.txt"
```
### 6. Install [phpMyAdmin](https://www.phpmyadmin.net/downloads/)
Establish MySql Connection and create database
```shell
cd smabuz
python3
from models import *
db.create_all()
db.session.commit()
```
### 7. Run Locally:
```shell
python3 main.py
```

### 8. Copy below links to your browser:
To see home page:
```html
http://localhost:5000  
```
To see login page:
```html
http://localhost:5000/login
```
To see signup page:
```html
http://localhost:5000/signup
```
