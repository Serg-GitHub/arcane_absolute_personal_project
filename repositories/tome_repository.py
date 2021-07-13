from db.run_sql import run_sql

from models.tome import Tome
from models.author import Author
import repositories.author_repository as author_repository

def save(tome):
    sql = "INSERT INTO tomes (title, genre, cost, quantity, price, author_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [tome.title, tome.genre, tome.cost, tome.quantity, tome.price, tome.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    tome.id = id
    return tome


def select_all():
    tomes = []

    sql = "SELECT * FROM tomes"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        tome = Tome(row['title'], row['genre'], row['cost'], row['quantity'], author, row['price'], row['id'] )
        tomes.append(tome)
    return tomes


def select(id):
    tome = None
    sql = "SELECT * FROM tomes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select(result['author_id'])
        tome = Tome(result['title'], result['genre'], result['cost'], result['quantity'], author, result['price'], result['id'])
        return tome


def delete_all():
    sql = "DELETE FROM tomes"
    run_sql(sql)

    
