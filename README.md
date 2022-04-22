# ShoppingListBackend
Shopping list backend using Python, Flask, SQLAlchemy.
2022

####
Create shopping list backend using Python, Flask, SQLAlchemy. Application should be object oriented, should obey SOLID principles, take clean architecture into consideration and use dependency injection. SQLite can be used as the storage database.

1. Option to create, edit, remove multiple shopping lists

2. Option to add, remove products to/from the list

3. Option to mark product as already purchased on the list
####

How to run?
```python
pip install flask
set FLASK_APP=lists.py
python -m flask run
```
```python
pip install flask-wtf
pip install wtforms
```
If you want to edit code :) 
```python
set FLASK_DEBUG=1
```

SQLALCHEMY
```python
pip install flask-sqlalchemy
```
and
```python
from lists import db
db.create_all()
```