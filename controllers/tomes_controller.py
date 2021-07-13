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