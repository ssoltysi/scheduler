import datetime

class ScheduleGenerator:

    def __init__(self, rounds, start_datetime, duration):
        self.rounds = rounds
        self.start_datetime = start_datetime
        self.duration = duration

    def generate_start_times(self):
        start_times = []
        round_time = self.duration/self.rounds

        for i in range(self.rounds):
            start_times.append(self.start_datetime +  i*round_time)

        return start_times


start = datetime.datetime(2015, 10, 1)
delta = datetime.timedelta(hours=2)
sg = ScheduleGenerator(4, start, delta)
print(sg.generate_start_times())
