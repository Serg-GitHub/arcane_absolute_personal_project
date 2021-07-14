from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tome import Tome
import repositories.tome_repository as tome_repository
import repositories.author_repository as author_repository

tomes_blueprint = Blueprint("tomes", __name__)

@tomes_blueprint.route("/tomes")
def tomes():
    tomes = tome_repository.select_all()
    return render_template("tomes/index.html", all_tomes = tomes)

@tomes_blueprint.route("/tomes/new", methods=['GET'])
def new_tome():
    authors = author_repository.select_all()
    return render_template("tomes/new.html", all_authors = authors)   

@tomes_blueprint.route("/tomes", methods=['POST'])
def create_tome():
    title = request.form['title']
    genre = request.form['genre']
    cost = request.form['cost']
    quantity = request.form['quantity']
    author = author_repository.select(request.form['author_id'])
    price = request.form['price']
    tome = Tome(title, genre, cost, quantity, author, price)
    tome_repository.save(tome)
    return redirect('/tomes') 

@tomes_blueprint.route("/tomes/<id>", methods=['GET'])
def show_tome(id):
    tome = tome_repository.select(id)
    return render_template('tome/show.html', tome = tome)    


@tomes_blueprint.route("/tomes/<id>/edit", methods=['GET'])
def edit_tome(id):
    tome = tome_repository.select(id)
    authors = author_repository.select_all()
    return render_template('tomes/edit.html', tome = tome, all_authors = authors)


@tomes_blueprint.route("/tomes/<id>", methods=['POST'])
def update_tome(id):
    title = request.form['title']
    genre = request.form['genre']
    cost = request.form['cost']
    quantity = request.form['quantity']
    author = author_repository.select(request.form['author_id'])
    price = request.form['price']
    tome = Tome(title, genre, cost, quantity, author, price, id)
    print(tome.author.full_name())
    tome_repository.update(tome)
    return redirect('/tomes')


@tomes_blueprint.route("/tomes/<id>/delete", methods=['POST'])
def delete_tome(id):
    tome_repository.delete(id)
    return redirect('/tomes')    

    


