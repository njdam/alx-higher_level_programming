<center> <h1>Python - Object-relational mapping</h1> </center>

Object-Relational Mapping (ORM) is a programming technique that allows developers to interact with relational databases using object-oriented programming languages like Python. Instead of writing raw SQL queries, developers can work with Python classes and objects to perform database operations, making it easier to manage and manipulate data.

One of the most popular Python ORM libraries is **SQLAlchemy**.

---

<center><h3>Overview of How SQLAlchemy Works</h3></center>

1. ***Installation:***

* You need to install SQLAlchemy first, typically using pip:
```
pip install sqlalchemy
```

* Import SQLAlchemy into your Python script or application:
```
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
```


2. ***Create a Database Engine:***

You need to create an engine that will connect to your database. The engine URL should specify the database type, location, and credentials.

```
# Example SQLite database
engine = create_engine('sqlite:///mydatabase.db')
```


3. ***Define Your Data Models:***

Create Python classes to represent your database tables. These classes should inherit from declarative_base() and define attributes that map to table columns.

```
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

# Create the table
Base.metadata.create_all(engine)
```


4. ***Session Creation:***

Create a session to interact with the database. A session acts as a unit of work and provides methods for querying and manipulating data.

```
Session = sessionmaker(bind=engine)
session = Session()
```


5. ***CRUD Operations:***

You can now use your defined classes and the session to perform CRUD (Create, Read, Update, Delete) operations on the database.


6. ***Creating Records:***

```
new_user = User(username='john_doe', email='john@example.com')
session.add(new_user)
session.commit()
```


7. ***Reading Records:***

```
user = session.query(User).filter_by(username='john_doe').first()
```


8. ***Updating Records:***

```
user.email = 'new_email@example.com'
session.commit()
```


9. ***Deleting Records:***

```
session.delete(user)
session.commit()
```


10. ***Closing the Session:***

Always close the session when you're done working with the database.

```
session.close()
```

[Note That:]() This is a basic overview of how SQLAlchemy, a popular ORM library, works in Python. It provides a high-level, Pythonic interface for database interactions, making it easier to work with databases in your applications. Depending on your project and requirements, you may explore more advanced features and configurations provided by SQLAlchemy.

