from flask import Flask
from flask import request
from flask import render_template
import db_driver
import datetime

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("db_form.html")

@app.route('/', methods=['POST'])
def my_form_post():

    date = request.form['date']
    time = request.form['time']
    duration = request.form['duration']
    weeks = request.form['weeks']
    rounds = request.form['rounds']
    teams = request.form['teams']
    location = request.form['location']
    sub_locations = request.form['sub_locations']

    duration = int(duration)
    weeks = int(weeks)
    rounds = int(rounds)
    teams = teams.split()
    sub_locations = sub_locations.split()

    date = date + ":" + time
    duration = datetime.timedelta(hours=duration)
    start_datetime = datetime.datetime.strptime(date, "%Y-%m-%d:%H:%M")

    db_driver.db_driver(teams, start_datetime, duration, rounds, weeks, location, sub_locations)

    return app.send_static_file('test.csv')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
