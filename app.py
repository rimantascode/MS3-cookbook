import os
from flask import Flask, flash, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.secret_key = "flashingmessages"
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def get_tasks():
    return render_template("index.html",
                           recipe=mongo.db.recipe.find())


@app.route('/index/<category>')
def get_categories(category):
    return render_template("index.html",
                           recipe=mongo.db.recipe.find({"category": category}))


@ app.route('/edit_recipe/<recipes_id>')
def edit_recipe(recipes_id):
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipes_id)})
    all_difficulties = mongo.db.difficulty.find()
    cooking_time = mongo.db.prep_time.find()
    return render_template('edit_recipe.html', recipes=the_recipe,
                           difficulties=all_difficulties, time=cooking_time, categoriess=mongo.db.categories.find())


@ app.route('/dish/<recipes_id>')
def dish(recipes_id):
    the_recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipes_id)})
    all_categories = mongo.db.categories.find()
    a = the_recipe["ingrediants"].split(",")
    return render_template('dish.html', recipes=the_recipe, a=a,
                           categories=all_categories,  image=mongo.db.recipe.find())


@ app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html',
                           levels=mongo.db.difficulty.find(), time=mongo.db.prep_time.find(),
                           categoriess=mongo.db.categories.find())


@ app.route('/insert_task', methods=['POST'])
def insert_recipe():
    tasks = mongo.db.recipe
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))


@ app.route('/update_task/<recipes_id>', methods=["POST"])
def update_recipe(recipes_id):
    recipe = mongo.db.recipe
    recipe.update({'_id': ObjectId(recipes_id)},
                  {
        'recipe_name': request.form.get('recipe_name'),
        'difficulty_level': request.form.get('difficulty_level'),
        'prep_time': request.form.get('prep_time'),
        'cooking_description': request.form.get('cooking_description'),
        'picture_url': request.form.get('picture_url'),
        "ingrediants": request.form.get('ingrediants')
    })
    return redirect(url_for('get_tasks'))


@ app.route('/delete_recipe/<recipes_id>')
def delete_recipe(recipes_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipes_id)})
    return redirect(url_for('get_tasks'))


@ app.route('/about_us')
def about_us():
    return render_template('about_us.html')


@ app.route('/contact_us')
def contact_us():
    return render_template("contact_us.html")


@ app.route("/contact_us_form", methods=['GET', 'POST'])
def contact_us_form():
    error = None
    if request.method == 'POST':
        if request.form['first_name'] == "":
            error = 'You must provide your name'
        else:
            flash('{}, Success! Thank you for contancting us.'.format(
                request.form['first_name']))
            return redirect(url_for("contact_us"))
    return render_template("contact_us.html", error=error)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
