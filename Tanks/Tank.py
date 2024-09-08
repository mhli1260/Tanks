from Vectors import*
class tank:
    def __init__(self, x, y, shooterangle, vel, fire, turn, lives, radius, fuel, r, g, b):
        self.x = x
        self.y = y
        self.shooterangle = shooterangle
        self.vel = vel
        self.fire = fire
        self.turn = turn
        self.lives = lives
        self.radius = radius
        self.fuel = fuel
        self.r = r
        self.g = g
        self.b = b
        
    def get_angle(self):
        return self.shooterangle
    def set_angle(self, angle):
        self.shooterangle = angle
    def set_vel(self, vel):
        self.vel = vel
    def set_posx(self, x):
        self.x = x
    def set_turn(self, turn):
        self.turn = turn
    def set_fire(self, fire):
        self.fire = fire
    def set_lives(self, lives):
        self.lives = lives
    def set_fuel(self, fuel):
        self.fuel = fuel
    def set_r(self, r):
        self.r = r
    def set_g(self, g):
        self.g = g
    def set_b(self, b):
        self.b = b
    def set_radius(self, radius):
        self.radius = radius
        
