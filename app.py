from flask import Flask
from flask import request
from flask import render_template
import driver

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my_form.html")

@app.route('/', methods=['POST'])
def my_form_post():

    date = request.form['date']
    time = request.form['time']
    rounds = request.form['rounds']
    teams = request.form['teams']
    duration = request.form['duration']
    byes = request.form['byes']

    duration = int(duration)
    rounds = int(rounds)
    teams = teams.split()
    byes = int(byes)

    driver.driver(date, time, duration, rounds, teams, byes)

    return app.send_static_file('test.csv')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
