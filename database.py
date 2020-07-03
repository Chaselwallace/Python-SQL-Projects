import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

CREATE_FAMILY_TABLE = """CREATE TABLE IF NOT EXISTS family
 (id SERIAL PRIMARY KEY, name TEXT, salary TEXT, location TEXT);"""
CREATE_CHILDREN_TABLE = """CREATE TABLE IF NOT EXISTS children
 (id SERIAL PRIMARY KEY, child_name TEXT, age TEXT, parent_id INTEGER,
 FOREIGN KEY(parent_id) REFERENCES family(id));"""
CREATE_CAR_TABLE = """CREATE TABLE IF NOT EXISTS cars (id SERIAL PRIMARY KEY, model TEXT, parent_id INTEGER,
 FOREIGN KEY(parent_id) REFERENCES family(id));"""

VIEW_FAMILY_PARENTS = "SELECT * FROM family;"
VIEW_TOTAL_FAMILY = "SELECT * FROM family LEFT JOIN children ON family.id = children.parent_id;"
VIEW_FAMILY_CAR = "SELECT family.id, family.name, cars.model FROM family LEFT JOIN cars ON family.id = cars.parent_id;"

INSERT_PARENT = "INSERT INTO family (name, salary, location) VALUES (%s, %s, %s);"
INSERT_CHILD = "INSERT INTO children (child_name, age, parent_id) VALUES (%s, %s, %s);"
INSERT_CAR = "INSERT INTO cars (model, parent_id) VALUES (%s, %s);"

connection = psycopg2.connect(os.environ["DATABASE_URL"])


def create_tables():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_FAMILY_TABLE)
            cursor.execute(CREATE_CHILDREN_TABLE)
            cursor.execute(CREATE_CAR_TABLE)


def insert_parent(name, salary, location):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_PARENT, (name, salary, location))


def insert_child(child_name, age, parent_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_CHILD, (child_name, age, parent_id))


def insert_car(model, parent_id):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_CAR, (model, parent_id))


def view_family():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(VIEW_FAMILY_PARENTS)
            return cursor.fetchall()


def view_cars():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(VIEW_FAMILY_CAR)
            return cursor.fetchall()


def view_children():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(VIEW_TOTAL_FAMILY)
            return cursor.fetchall()
