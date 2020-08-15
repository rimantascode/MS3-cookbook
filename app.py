import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def get_tasks():
    list = mongo.db.recipe.find()
    for n in list:
        s = n["ingrediants"].split(",")
    return render_template("index.html",
                           recipe=mongo.db.recipe.find(), s=s)


@app.route('/dish')
def dish():
    list = mongo.db.recipe.find()
    for n in list:
        s = n["ingrediants"].split(",")
    return render_template("dish.html", recipe=mongo.db.recipe.find(), s=s, description=mongo.db.recipe.find(), image=mongo.db.recipe.find())


@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                           categ=mongo.db.difficulty.find(), time=mongo.db.prep_time.find())


@app.route('/insert_task', methods=['POST'])
def insert_recipe():
    tasks = mongo.db.recipe
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
