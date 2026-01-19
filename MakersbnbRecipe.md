```

# makersbnb Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](https://journey.makers.tech/pages/single-table-design-recipe-template).

*In this template, we will use an example table `students`*

```

# EXAMPLE

Table: users
id | name | email_address | pw  | created_at 



Table: listings 
id | name | location | dates  | user_id (FK) | short_description | price_per_day  | created_at

Bookings: 

id  | listing_id (FK)  | user_id (FK)  | start_date  | end_date  | status (pending, confirmed, rejected) | created_at 


Table: availability -VAGUE IDEA (summarising all bookings submitted to calculate availability) 

id (primary) | listing_id(FK) | start_date  | end_date  | status (pending, confirmed, rejected)  | created_at 


```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql

-- EXAMPLE
-- (file: spec/seeds_{table_name}.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE students RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO students (name, cohort_name) VALUES ('David', 'April 2022');
INSERT INTO students (name, cohort_name) VALUES ('Anna', 'May 2022');

```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: students

# Model class
# (in lib/student.py)
class Student


# Repository class
# (in lib/student_repository.py)
class StudentRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python

# EXAMPLE
# Table name: students

# Model class
# (in lib/student.py)

class User:
    def __init__(self, id, name, email_address, pw,  created_at=None):
        self.id = id
        self.name = name
        self.email_address = email_address
        self.created_at = created_at

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User ({self.id}, {self.name}, {self.email_address})"



class Bookings:
    def __init__(self, < listing_id FK>, < user_id FK> , start_date,  end_date, status, created_at=None):
        self.id = id
        self.listing_id = listing_id # FK
        self.user_id = user_id # FK
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.created = created_at


    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Booking ({self.id}, {self.listing_id}, {self.user_id}, {self.start_date}, {self.end_date}, {self.status},{self.created_at})"



class Listing:
    def __init__(self, name, location, dates, < user_id FK (host)> , short_description,  price_per_day, created_at=None):
        self.id = id
        self.name = name
        self.dates = dates # we need to have a think about how this can work - we need to record the dates that a property is available 
        self.user_id = user_id # FK
        self.short_description = short_description
        self.price_per_day = price_per_day
        self.created = created_at


    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f" Listing ({self.id}, {self.name}, {self.dates}, {self.user_id}, {self.short_description}, {self.price_per_day},{self.created_at})"



# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> student = Student()
# >>> student.name = "Will"
# >>> student.cohort_name = "September Devs"
# >>> student.name
# 'Will'
# >>> student.cohort_name
# 'September Devs'

```

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python

# Repository class
# (in lib/user_repository.py)

class UserRepository()

    def create(user):
        # INSERT INTO users (id | name | email_address | pw  | created_at);
        VALUES(%s, %s, %s, %s, %s )

    def find(id):
        # Executes the SQL query:
        # SELECT id | name | email_address | pw  FROM users WHERE email = %s

        # Returns a single User object.



# Listing Class
# (in lib/listing_repository.py) 

class ListingsRepository():

    def all():
        # Executes the SQL query:
        # SELECT id, name, location, dates, user_id (FK), Description, price_per_day, created_at FROM listings;
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s )

        # Returns an array of Listing objects.

    def find(id):
        # Route: makersbnb/listings/4
        # Executes the SQL query:
        # SELECT (id, name, location, dates, user_id (FK), Description, price_per_day, created_at WHERE id = %s;
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s )

    
    def find(user_id):
        # Route: makersbnb/listings/4
        # Executes the SQL query:
        # SELECT (id, name, location, dates, user_id (FK), Description, price_per_day, created_at WHERE id = %s;
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s )

    

    # #  Do updates and deletes as nice to haves 

# Booking Class
# (in lib/booking_repository.py) 

class BookingsRepository():

    def create(booking):
        # INSERT INTO bookings ( id  | listing_id (FK)  | user_id (FK)  | start_date  | end_date  | status (pending, confirmed, rejected) | created_at );
        VALUES(%s, %s, %s, %s, %s, %s, %s)

    def all():
        # Executes the SQL query:
        # SELECT id  | listing_id (FK)  | user_id (FK)  | start_date  | end_date  | status (pending, confirmed, rejected) | created_at );
        VALUES(%s, %s, %s, %s, %s, %s, %s)


    def find(id):
        # SELECT id  | listing_id (FK)  | user_id (FK)  | start_date  | end_date  | status (pending, confirmed, rejected) | created_at WHERE id = %s;
        VALUES(%s, %s, %s, %s, %s, %s, %s)

#How do we pull up just the records in the bookings table that relate to the hosts properties (so they are not seeing ALL bookings) - what do we run the find search on? 
Idea 1: define whether user is host or guest, search on that user Id 
Idea 2: 2 joins, use listing_id to pull in host name 

```



## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all students

repo = StudentRepository()

students = repo.all()

len(students) # =>  2

students[0].id # =>  1
students[0].name # =>  'David'
students[0].cohort_name # =>  'April 2022'

students[1].id # =>  2
students[1].name # =>  'Anna'
students[1].cohort_name # =>  'May 2022'

# 2
# Get a single student

repo = StudentRepository()

student = repo.find(1)

student.id # =>  1
student.name # =>  'David'
student.cohort_name # =>  'April 2022'

# Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._