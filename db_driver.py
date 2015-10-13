import datetime
import schedule_generator
import round_robin_generator
import csv
import sys
import random


def db_driver(teams, start_datetime, duration, rounds, number_of_weeks, location, sublocations):
    write_csv_header()
    one_week_delta = datetime.timedelta(weeks=1)
    date = start_datetime
    
    for i in range(number_of_weeks):
        random.shuffle(teams)
        number_of_teams = len(teams)
        wave1 = teams[0:number_of_teams/2]
        wave2 = teams[number_of_teams/2:number_of_teams]

        date_wave1 = date
        date_wave2 = date + duration/2

        create_schedule_for_wave(wave1, date_wave1, rounds, duration/2, location, sublocations)
        create_schedule_for_wave(wave2, date_wave2, rounds, duration/2, location, sublocations)        

        date += one_week_delta

def write_csv_header():
    with open("static/test.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerow( ('Team A', 'Team B', 'Time', 'Date', 'Location', 'SubLocation') )


def create_schedule_for_wave(wave, date, rounds, duration, location, sublocations):
    rrg = round_robin_generator.RRMatchupGenerator(wave, rounds)
    matchups = rrg.generate_matchups()
    
    sg = schedule_generator.ScheduleGenerator(rounds, date, duration)
    times = sg.generate_start_times()

    with open("static/test.csv", 'a') as file:
        writer = csv.writer(file)

        for i in range(len(times)):
            time = times[i]
            date = time.strftime("%Y-%m-%d")
            time = time.strftime("%H:%M")
            round_matchups = matchups[i]

            j = 0
            for matchup in round_matchups:
                writer.writerow((matchup[0], matchup[1], time, date, location, sublocations[j]))
                j += 1

if __name__ == "__main__":
    teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    number_of_weeks = 2
    start_date = datetime.datetime(2015,10,10)
    rounds = 3
    duration = datetime.timedelta(hours=2)
    location = 'Somewhere'
    sublocations = ['CourtA', 'CourtB']

    db_driver(teams, number_of_weeks, start_date, rounds, duration, location, sublocations)
