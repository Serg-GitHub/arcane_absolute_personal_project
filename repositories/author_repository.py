# from the database run_sql import self
from db.run_sql import run_sql

# from the models directory, import the Author class from the author.py file
from models.author import Author
# from the models directory, import the Tome class from the tome.py file
from models.tome import Tome

def save(author):
    sql = "INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [author.first_name, author.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author


def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values =[id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result['first_name'], result['last_name'], result['id'])
        return author


def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['first_name'], row['last_name'], row['id'])
        authors.append(author)
    return authors            



def delete_all():
    sql = "DELETE  FROM authors"
    run_sql(sql)    
