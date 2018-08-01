# Team 1 has 1 ball
# Team 2 has 2 balls
# ...
# Team 32 has 32 balls

# If the same ball is taken out, we keep drawing until another team
import random

class Draft:
    def __init__(self, number_of_teams = 32):
        self.number_of_teams = number_of_teams
        self.balls = {x: x for x in range(1, self.number_of_teams + 1)}
        self.total_balls = sum(x for x in range(1, self.number_of_teams + 1))
        self.prob = {}
        self.update_prob()
        self.current_pos = 1
        self.drew = {x:-1 for x in range(1, self.number_of_teams + 1)}

    def update_prob(self):
        self.prob = {x: self.balls[x] / self.total_balls for x in range(1, self.number_of_teams + 1)}

    def draw(self):
        rand_val = random.random()
        total = 0
        for k, v in self.prob.items():
            total += v
            if rand_val <= total:
                self.update(k)
                return k

    def update(self, team):
        self.balls[team] -= 1
        self.total_balls -= 1
        if self.total_balls > 0:
            self.update_prob()

    def draw_new(self):
        team = self.draw()
        if self.drew[team] != -1:
            return self.draw_new()
        else:
            self.drew[team] = self.current_pos
            self.current_pos += 1
            return team

    def draw_all(self):
        for i in range(32):
            d.draw_new()


N = 100
count = 0
for i in range(N):
    d = Draft()
    d.draw_all()
    if((d.drew[30] == 1 or d.drew[30] == 2 or d.drew[30] == 3)
            and (d.drew[28] == 1 or d.drew[28] == 2 or d.drew[28] == 3)
            and (d.drew[11] == 1 or d.drew[11] == 2 or d.drew[11] == 3)):
        count+=1

print(count)


