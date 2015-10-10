import datetime
import schedule_generator
import round_robin_generator
import csv
import sys

def driver(date, time, duration, rounds, teams, byes):
    #rounds = 4
    #day = "2015-10-1"
    #time_of_day = 19
    #duration = 2

    date = date + ":" + time
    #time = datetime.timedelta(hours=time)
    duration = datetime.timedelta(hours=duration)
    date = datetime.datetime.strptime(date, "%Y-%m-%d:%H:%M")

    sg = schedule_generator.ScheduleGenerator(rounds, date, duration)
    times = sg.generate_start_times()
    print(times)

    rrg = round_robin_generator.RRMatchupGenerator(teams, rounds, byes)
    
    matchups = rrg.generate_matchups()
    print(matchups)

    with open("static/test.csv", 'wt') as file:
        writer = csv.writer(file)
        writer.writerow( ('Team A', 'Team B', 'Time', 'Date') )

        for i in range(len(times)):
            time = times[i]
            date = time.strftime("%Y-%m-%d")
            time = time.strftime("%H:%M")
            round_matchups = matchups[i]

            for matchup in round_matchups:
                writer.writerow((matchup[0], matchup[1], time, date))
