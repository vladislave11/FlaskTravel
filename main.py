from flask import Flask, render_template, request, abort, make_response, redirect, url_for
import sqlite3
import os
# import data
app = Flask(__name__)

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect(database='booking.db')
    connection.row_factory = sqlite3.Row
    return connection



titles = {'title': '',
          'subtitle': '',
          'description': ''}



connection = get_db_connection()
title = connection.execute('SELECT * FROM titles')

for i in title:
    titles['title'] = i['title']
    titles['subtitle'] = i['subtitle']
    titles['description'] = i['description']



departuress = {}
# connection = get_db_connection()
city = connection.execute('SELECT * FROM cities')

for k in city:
    departuress[k['city']] = k['city_link']




tourss = {
    1: {"title": '',
"description": '',
"departure": '',
"picture": '',
"price": 0,
"stars": '',
"country": '',
"nights": '',
"date": ''},
    2: {"title": '',
"description": '',
"departure": '',
"picture": '',
"price": 0,
"stars": '',
"country": '',
"nights": '',
"date": ''},
    3: {"title": '',
"description": '',
"departure": '',
"picture": '',
"price": 0,
"stars": '',
"country": '',
"nights": '',
"date": ''},
    4: {"title": '',
"description": '',
"departure": '',
"picture": '',
"price": 0,
"stars": '',
"country": '',
"nights": '',
"date": ''},
    5: {"title": '',
"description": '',
"departure": '',
"picture": '',
"price": 0,
"stars": '',
"country": '',
"nights": '',
"date": ''},
    6: {"title": '',
"description": '',
"departure": '',
"picture": '',
"price": 0,
"stars": '',
"country": '',
"nights": '',
"date": ''},
    7: {"title": '',
"description": '',
"departure": '',
"picture": '',
"price": 0,
"stars": '',
"country": '',
"nights": '',
"date": ''},
    8: {"title": '',
"description": '',
"departure": '',
"picture": '',
"price": 0,
"stars": '',
"country": '',
"nights": '',
"date": ''}
}


tour1 = connection.execute('SELECT * FROM tour_1')
tour2 = connection.execute('SELECT * FROM tour_2')
tour3 = connection.execute('SELECT * FROM tour_3')
tour4 = connection.execute('SELECT * FROM tour_4')
tour5 = connection.execute('SELECT * FROM tour_5')
tour6 = connection.execute('SELECT * FROM tour_6')
tour7 = connection.execute('SELECT * FROM tour_7')
tour8 = connection.execute('SELECT * FROM tour_8')



for el in tour1:
    tourss[1]['title'] = el['title']
    tourss[1]['description'] = el['description']
    tourss[1]['departure'] = el['departure']
    tourss[1]['picture'] = el['picture']
    tourss[1]['price'] = el['price']
    tourss[1]['stars'] = el['stars']
    tourss[1]['country'] = el['country']
    tourss[1]['nights'] = el['nights']
    tourss[1]['date'] = el['date']

for el in tour2:
    tourss[2]['title'] = el['title']
    tourss[2]['description'] = el['description']
    tourss[2]['departure'] = el['departure']
    tourss[2]['picture'] = el['picture']
    tourss[2]['price'] = el['price']
    tourss[2]['stars'] = el['stars']
    tourss[2]['country'] = el['country']
    tourss[2]['nights'] = el['nights']
    tourss[2]['date'] = el['date']
    break

for el in tour3:
    tourss[3]['title'] = el['title']
    tourss[3]['description'] = el['description']
    tourss[3]['departure'] = el['departure']
    tourss[3]['picture'] = el['picture']
    tourss[3]['price'] = el['price']
    tourss[3]['stars'] = el['stars']
    tourss[3]['country'] = el['country']
    tourss[3]['nights'] = el['nights']
    tourss[3]['date'] = el['date']

for el in tour4:
    tourss[4]['title'] = el['title']
    tourss[4]['description'] = el['description']
    tourss[4]['departure'] = el['departure']
    tourss[4]['picture'] = el['picture']
    tourss[4]['price'] = el['price']
    tourss[4]['stars'] = el['stars']
    tourss[4]['country'] = el['country']
    tourss[4]['nights'] = el['nights']
    tourss[4]['date'] = el['date']

for el in tour5:
    tourss[5]['title'] = el['title']
    tourss[5]['description'] = el['description']
    tourss[5]['departure'] = el['departure']
    tourss[5]['picture'] = el['picture']
    tourss[5]['price'] = el['price']
    tourss[5]['stars'] = el['stars']
    tourss[5]['country'] = el['country']
    tourss[5]['nights'] = el['nights']
    tourss[5]['date'] = el['date']

for el in tour6:
    tourss[6]['title'] = el['title']
    tourss[6]['description'] = el['description']
    tourss[6]['departure'] = el['departure']
    tourss[6]['picture'] = el['picture']
    tourss[6]['price'] = el['price']
    tourss[6]['stars'] = el['stars']
    tourss[6]['country'] = el['country']
    tourss[6]['nights'] = el['nights']
    tourss[6]['date'] = el['date']

for el in tour7:
    tourss[7]['title'] = el['title']
    tourss[7]['description'] = el['description']
    tourss[7]['departure'] = el['departure']
    tourss[7]['picture'] = el['picture']
    tourss[7]['price'] = el['price']
    tourss[7]['stars'] = el['stars']
    tourss[7]['country'] = el['country']
    tourss[7]['nights'] = el['nights']
    tourss[7]['date'] = el['date']

for el in tour8:
    tourss[8]['title'] = el['title']
    tourss[8]['description'] = el['description']
    tourss[8]['departure'] = el['departure']
    tourss[8]['picture'] = el['picture']
    tourss[8]['price'] = el['price']
    tourss[8]['stars'] = el['stars']
    tourss[8]['country'] = el['country']
    tourss[8]['nights'] = el['nights']
    tourss[8]['date'] = el['date']





@app.route('/')
def index():
    return render_template('index.html',
                           title = titles['title'],
                           departures = departuress,
                           description = titles['description'],
                           subtitle = titles['subtitle'],
                           tours = tourss,
                           cookie = request.cookies.get('username'))


@app.route('/departures/')
def departures():
    return render_template('departure.html')


@app.route('/departures/<departure>/')
def departure(departure):
    global tours
    tours = dict(filter(lambda tour: tour[1]["departure"] == departure, tourss.items()))
    if tours:
        return render_template('departure.html',
                               departure=departure,
                               title = titles['title'],
                               departures = departuress,
                               tours = tourss)
    abort(404)
@app.route('/tours/')
def list_tours():
    return render_template('tour.html')


@app.route('/tours/<int:id>/')
def tours(id):
    return render_template('tour.html',
                           tour = tourss[id],
                           title = titles['title'],
                           departures = departuress)

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if not request.cookies.get('username') and request.method == 'POST':
        res = make_response('Setting a cookie')
        res.set_cookie('username', request.form.get('name'), max_age=60*60*24*365*2)
        return res
    return render_template('login.html')

@app.route('/cookie/')
def cookie():
    if not request.cookies.get('username') or request.cookies.get('username') == 'None':
        return redirect(url_for('login.html'))
    else:
        res = make_response(f"Value of cookie is {request.cookies.get('username')}")
        return res


@app.route('/agent/')
def agent():
    user_agent = request.headers.get('User-Agent')
    return f'<b>Your browser is {user_agent}</b>'


app.run(port=5050, debug=True)

@app.route('/')
def index():
    return render_template('index.html',
                           title = titles['title'],
                           departures = departuress,
                           description = titles['description'],
                           subtitle = titles['subtitle'],
                           tours = tourss,
                           cookie = request.cookies.get('username'))


@app.route("/departures/")
def departure():
    return render_template("departure.html")


@app.route('/departures/<departure>/')
def departure(departure):
    global tours
    tours = dict(filter(lambda tour: tour[1]["departure"] == departure, tourss.items()))
    if tours:
        return render_template('departure.html',
                               departure=departure,
                               title = titles['title'],
                               departures = departuress,
                               tours = tourss)
    abort(404)


@app.route("/tours/")
def list_tours():
    return render_template("tour.html")


@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if not request.cookies.get('username') and request.method == 'POST':
        res = make_response('Setting a cookie')
        res.set_cookie('username', request.form.get('name'), max_age=60*60*24*365*2)
        return res
    return render_template('login.html')


@app.route("/login/", methods=["GET", "POST"])
def login():
    if not request.cookies.get("username") and request.method == "POST":
        res = make_response("Setting a cookie")
        res.set_cookie("username", request.form.get("name"), max_age=60 * 60 * 24 * 365 * 2)
        return res
    return render_template("login.html")

@app.route("/cookie/")
def cookie():
    if not request.cookies.get("username") or request.cookies.get("username") == "None":
        return redirect(url_for("login"))
    else:
        res = make_response(f"Value of cookie is {request.cookies.get('username')}")
        return res

@app.route("/agent/")
def agent():
    user_agent = request.headers.get("User-Agent")
    return f"<b>Your browser is {user_agent}</b>"


app.run(port=35023, debug=True)