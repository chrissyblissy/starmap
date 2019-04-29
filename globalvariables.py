import random, math

newgamecash = cash = 0
newgamefuel = fuel = 10500

game_running = True
firstgame = True
last_mission = 11

enemyshipcreated = False

class ship(object):
    "Creates spaceships"
    def __init__(self, position_x, position_y, bearing, movement_x, movement_y):
        self.position_x = position_x
        self.position_y = position_y
        self.bearing = bearing
        self.movement_x = movement_x
        self.movement_y = movement_y

    def calc_bearing(self):
        if self.movement_y == 0 and self.movement_x == 0:
            self.bearing = 0
        elif self.movement_y == 0 and self.movement_x > 0:
            self.bearing = 270
        elif self.movement_y == 0 and self.movement_x < 0:
            self.bearing = 90
        elif self.movement_y < 0:
            self.bearing = math.degrees(math.atan(-self.movement_x / -self.movement_y))
        else:
            self.bearing = math.degrees(math.atan(-self.movement_x / -self.movement_y)) + 180

    def calc_border(self, border, y_max, x_max):
        if self.position_y < border:
            self.position_y += y_max     
        if self.position_y > y_max:
            self.position_y -= y_max 
        if self.position_x < border:
            self.position_x += x_max
        if self.position_x > x_max:
            self.position_x -= x_max

    def total_movement(self):
        return abs(self.movement_y) + abs(self.movement_x)
