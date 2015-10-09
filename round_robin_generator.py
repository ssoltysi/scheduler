class RRMatchupGenerator:

    def __init__(self, teams, rounds, byes=0):
        
        is_odd_number_of_teams = len(teams)%2 == 1

        if is_odd_number_of_teams and byes == 0:
            teams.append("BYE")

        if byes > 0:
            for i in range(byes):
                teams.insert(0, "BYE")

        self.rounds = rounds
        self.teams = teams
        self.matchups = []

    def rr_algorithm_generator(self):
        
        for i in range(self.rounds):
            yield self.teams
            end = self.teams.pop()
            self.teams.insert(1, end)

    def generate_matchups_for_round(self, teams):
        number_of_teams = len(teams)
        matchups = []
        
        for index in range(number_of_teams//2):
            pairing = teams[index], teams[number_of_teams - index -1]
            matchups.append(pairing)
            
        return matchups

    def generate_matchups(self):
        matchups = []
        for teams in self.rr_algorithm_generator():
            matchups_for_round = self.generate_matchups_for_round(teams)
            matchups.append(matchups_for_round)

        return matchups

l = [1,2,3,4,5,6,7,8]
rrg = RRMatchupGenerator(l, 2)

print(l)

for item in rrg.rr_algorithm_generator():
    print(item)

matchups = rrg.generate_matchups()
print(matchups)

    #matchups = rrg.generate_matchups()
    #print(matchups)
