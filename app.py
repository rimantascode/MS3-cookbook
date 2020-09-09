#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask, flash, render_template, redirect, request, \
    url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_share import Share
from datetime import datetime, timedelta
import humanize
from flask_paginate import Pagination, get_page_parameter, get_page_args
from flask import Blueprint

mod = Blueprint('users', __name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')
app.config['MONGO_DBNAME'] = 'cook_book'
app.config['MONGO_URI'] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)
share = Share()
share.init_app(app)


@app.route('/')
@app.route('/index')
def get_tasks():
    time_added()
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 4
    offset = (page - 1) * per_page

    recipe = mongo.db.recipe.find().sort('date',
            -1).skip(offset).limit(per_page)
    pagination = Pagination(
        page=page,
        total=recipe.count(),
        search=search,
        record_name='Recipes',
        offset=offset,
        per_page=per_page,
        )

    return render_template('index.html', recipe=recipe,
                           pagination=pagination,
                           added_latest=time_added(),
                           all_recipes='All recipes')


@app.route('/index/<category>')
def get_categories(category):
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), type=int, default=1)
    per_page = 4
    offset = (page - 1) * per_page

    recipes = mongo.db.recipe.find({'category': category})
    pagination = Pagination(
        page=page,
        total=recipes.count(),
        search=search,
        record_name='recipes',
        offset=offset,
        per_page=per_page,
        )

    return render_template(
        'index.html',
        recipe=mongo.db.recipe.find({'category': category}).sort('date'
                , -1).skip(offset).limit(per_page),
        added_latest=time_added(),
        category=category,
        pagination=pagination,
        hidden='hidden',
        )


@app.route('/edit_recipe/<recipes_id>')
def edit_recipe(recipes_id):
    the_recipe = mongo.db.recipe.find_one({'_id': ObjectId(recipes_id)})
    all_difficulties = mongo.db.difficulty.find()
    cooking_time = mongo.db.prep_time.find()
    return render_template('edit_recipe.html', recipes=the_recipe,
                           difficulties=all_difficulties,
                           time=cooking_time,
                           categoriess=mongo.db.categories.find())


@app.route('/dish/<recipes_id>')
def dish(recipes_id):
    the_recipe = mongo.db.recipe.find_one({'_id': ObjectId(recipes_id)})
    all_categories = mongo.db.categories.find()
    a = the_recipe['ingrediants'].split(',')
    return render_template('dish.html', recipes=the_recipe, a=a,
                           categories=all_categories,
                           image=mongo.db.recipe.find())


@app.route('/add_recipe')
def add_recipe():
    x = datetime.now()
    return render_template('add_recipe.html',
                           levels=mongo.db.difficulty.find(),
                           time=mongo.db.prep_time.find(),
                           categoriess=mongo.db.categories.find(),
                           date=x)


@app.route('/insert_task', methods=['POST'])
def insert_recipe():
    if request.method == 'POST':
        ingrediants_len = len(request.form['ingrediants'])
        if len(request.form['ingrediants']) < 200:
            ingrediants = request.form['ingrediants'] + ' ' * (200
                    - ingrediants_len)
        else:
            ingrediants = request.form['ingrediants']
    x = str(datetime.now())
    tasks = mongo.db.recipe
    tasks.insert_one({
        'recipe_name': request.form.getlist('recipe_name')[0].upper(),
        'difficulty_level': request.form.get('difficulty_level'),
        'prep_time': request.form.get('prep_time'),
        'cooking_description': request.form.get('cooking_description'),
        'picture_url': request.form.get('picture_url'),
        'ingrediants': ingrediants,
        'category': request.form.get('category'),
        'date': x,
        })

    return redirect(url_for('get_tasks'))


@app.route('/update_task/<recipes_id>', methods=['POST'])
def update_recipe(recipes_id):
    if request.method == 'POST':
        ingrediants_len = len(request.form['ingrediants'])
        if len(request.form['ingrediants']) < 200:
            ingrediants = request.form['ingrediants'] + ' ' * (200
                    - ingrediants_len)
        else:
            ingrediants = request.form['ingrediants']
    x = str(datetime.now())
    recipe = mongo.db.recipe
    recipe.update({'_id': ObjectId(recipes_id)}, {
        'recipe_name': request.form.get('recipe_name').upper(),
        'difficulty_level': request.form.get('difficulty_level'),
        'prep_time': request.form.get('prep_time'),
        'cooking_description': request.form.get('cooking_description'),
        'picture_url': request.form.get('picture_url'),
        'ingrediants': ingrediants,
        'category': request.form.get('category'),
        'date': x,
        })
    return redirect(url_for('get_tasks'))


@app.route('/delete_recipe/<recipes_id>')
def delete_recipe(recipes_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipes_id)})
    return redirect(url_for('get_tasks'))


@app.route('/about_us')
def about_us():
    return render_template('about_us.html', about_us='About Us',
                           hidden='hidden')


@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html', contact_us='Contact Us',
                           hidden='hidden')


@app.route('/contact_us_form', methods=['GET', 'POST'])
def contact_us_form():
    error = None
    if request.method == 'POST':
        if request.form['first_name'] == '':
            error = 'You must provide your name'
        else:
            flash('{}, Success! Thank you for contacting us.'.format(request.form['first_name'
                  ]))
            return redirect(url_for('contact_us'))
    return render_template('contact_us.html', error=error)


def time_added():
    lists = []
    list2 = []
    dicts = {}
    a = mongo.db.recipe.find().sort('date', -1)
    for z in a:
        j = z['date']
        x = datetime.today()
        l = datetime.strptime(j, '%Y-%m-%d %H:%M:%S.%f')
        v = x - l
        i = v.total_seconds()
        o = str(humanize.naturaltime(i))
        if i < 86400:
            lists.append([o, 'new'])
            list2.append(j)
        else:
            lists.append(o)
            list2.append(j)
        keys = range(0, len(lists))
    for b in keys:
        dicts[list2[b]] = [lists[b]]
    return dicts


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(os.environ.get('PORT'
            )), debug=True)
