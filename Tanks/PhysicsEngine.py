from Vectors import*
from Shooter import*
from Tank import*
from Tower import*
from Birds import*
from Powerups import*
counter2 = 0
counter1 = 0
turn = 2
scl = 30
tank1 = tank(700, -700, 0, 0, False, 1, 3, 10, 100, 255, 0, 0)
tank2 = tank(200, -700, 0, 0, False, 0, 3, 10, 100, 0, 0, 255) 
tower = tower(random(300, 600), -700, 30, random(30, 200))
bird1 = bird(random(300, 600), random(-650, -400), random(1, 30), 10)
bird2 = bird(random(300, 600), random(-650, -400), random(1, 30), 10)
bird3 = bird(random(300, 600), random(-650, -400), random(1, 30), 10)
power1 = power(random(300, 400), random(-650, -400), 255, 0, 0)
power2 = power(random(400, 500), random(-650, -400), 0, 255, 0)
power3 = power(random(500, 600), random(-650, -400), 0, 0, 255)

#setting up for projectile
radius = 0.125
m = 5
C = 0.3
A = PI * radius * radius
t = 0
dt = 0.01
p = 1.2

a = Vec(0,-9.8,0)
w2 = Vec(random(0,40),0,0)
w1 = Vec(random(-40,0), 0,0)
Fg = Vec.Vmul(a, m)
F = Vec(0,0,0)


r2 = Vec(0,0,0)
v2 = Vec(0,0,0)
r1 = Vec(0,0,0)
v1 = Vec(0,0,0)
powerUp = False
cloud1 = Vec(1200,200,0)
cloud2 = Vec(700, 200, 0)
cloud3 = Vec(300, 200, 0)
cloud4 = Vec(0,200,0)
cloud5 = Vec(400, 200, 0)
cloud6 = Vec(800, 200, 0)

#projectile for blue tank
def move2():
    dt = 0.1
    global counter2, scl, r2, v2, turn, fire, powerUp
    if (counter2 == 0):
        powerUp = True
        r2 = Vec(tank2.x + cos(radians(tank2.shooterangle))*scl+30, tank2.y+sin(radians(tank2.shooterangle))*scl+30, 0)            
        v2 = Vec(tank2.vel*cos(radians(tank2.shooterangle)),tank2.vel*sin(radians(tank2.shooterangle)), 0)
        counter2 += 1
    global t, C, A
    t += dt
    # T = 15.04 - (0.00649*r.y)
    # P = 101.29*((((T+273.1)/288.08))**5.256)
    # p = P/(0.2869*(T+273.1))
                    
    s = Vec.Vsub(v2,w2)
    d = ((C*A*p*(Vec.Vmag(s)**2))/2)
    Fd = Vec.Vmul(Vec.Vnorm(Vec.Vsub(v2,w2)), -1*d)
    F = Vec.Vadd(Fd, Fg)
    a = Vec.Vdiv(F, m)
    Vec.Vadd2(v2, Vec.Vmul(a, dt))
    Vec.Vadd2(r2, Vec.Vmul(v2, dt))
    ellipse(r2.x, r2.y, tank2.radius, tank2.radius)
    
    if (r2.x >= tank1.x-tank2.radius and r2.x <= tank1.x+40+tank2.radius and r2.y <= -670+tank2.radius):
        # tank1.set_lives(tank1.lives - 1)
        # print(tank1.lives)
        dt = 0
        tank2.set_turn(tank2.turn + 1)
        counter2 = 0
        tank2.set_fire(False)
        if (Vec.Vmag(v2) >= 60):
            tank1.set_fuel(tank1.fuel - 40)
        elif (Vec.Vmag(v2) >= 50):
            tank1.set_fuel(tank1.fuel - 20)
        elif(Vec.Vmag(v2) >= 40):
            tank1.set_fuel(tank1.fuel - 10)
        else:
            tank1.set_fuel(tank1.fuel - 5)
            
    elif(r2.y <= -700 + tank2.radius):
        tank2.set_turn(tank2.turn + 1)
        dt = 0
        counter2 = 0
        tank2.set_fire(False)
        
    elif(r2.x >= tower.x-tank2.radius and r2.x <= tower.x+tower.w-tank2.radius and r2.y <= tower.y+tower.h+tank2.radius):
        tank2.set_turn(tank2.turn + 1)
        dt = 0
        counter2 = 0
        tank2.set_fire(False)
        
    elif (r2.x >= bird1.posx - tank2.radius and r2.x <= bird1.posx + 30 + tank2.radius and r2.y >= bird1.posy - tank2.radius and r2.y <= bird1.posy+10+tank2.radius):
        dt = 0
        tank2.set_turn(tank2.turn + 1)
        counter2 = 0
        tank2.set_fire(False)
        bird1.set_posx(-50)
        bird1.set_velx(0)

    elif (r2.x >= bird2.posx-tank2.radius and r2.x <= bird2.posx + 30 + tank2.radius and r2.y >= bird2.posy-tank2.radius and r2.y <= bird2.posy+10+tank2.radius):
        dt = 0
        tank2.set_turn(tank2.turn + 1)
        counter2 = 0
        tank2.set_fire(False)
        bird2.set_posx(-50)
        bird2.set_velx(0)

    elif (r2.x >= bird3.posx-tank2.radius and r2.x <= bird3.posx + 30 + tank2.radius and r2.y >= bird3.posy-tank2.radius and r2.y <= bird3.posy+10+tank2.radius):
        dt = 0
        tank2.set_turn(tank2.turn + 1)
        counter2 = 0
        tank2.set_fire(False)
        bird3.set_posx(-50)
        bird3.set_velx(0)
        
    elif (r2.x >= power1.posx - tank2.radius and r2.x <= power1.posx + 15 + tank2.radius and r2.y <= power1.posy + tank2.radius and r2.y >= power1.posy - 15 - tank2.radius and powerUp == True):
        tank2.set_fuel(tank2.fuel + 20)
        powerUp = False

        print("hai")
    elif (r2.x >= power2.posx - tank2.radius and r2.x <= power2.posx + 15 + tank2.radius and r2.y <= power2.posy + tank2.radius and r2.y >= power2.posy - 15 - tank2.radius and powerUp == True):
        tank2.set_radius(tank2.radius + 3)
        powerUp = False
        print(tank2.radius)

    elif (r2.x >= power3.posx - tank2.radius and r2.x <= power3.posx + 15 + tank2.radius and r2.y <= power3.posy + tank2.radius and r2.y >= power3.posy - 15 - tank2.radius and powerUp == True):
        tank2.set_radius(tank2.radius - 3)
        powerUp = False
        print(tank2.radius)
    
#projectile for red tank
def move1():
    dt = 0.1
    global counter1, scl, r1, v1, turn, fire, powerUp
    print(counter1)
    if (counter1 == 0):
        powerUp = True
        r1 = Vec(tank1.x - cos(radians(tank1.shooterangle))*scl, tank1.y+sin(radians(tank1.shooterangle))*scl+30, 0)
        v1 = Vec(-tank1.vel*cos(radians(tank1.shooterangle)),tank1.vel*sin(radians(tank1.shooterangle)), 0)
        counter1 += 1
    global t, C, A
    t += dt
                    
    s = Vec.Vsub(v1,w1)
    d = ((C*A*p*(Vec.Vmag(s)**2))/2)
    Fd = Vec.Vmul(Vec.Vnorm(Vec.Vsub(v1,w1)), -1*d)
    F = Vec.Vadd(Fd, Fg)
    a = Vec.Vdiv(F, m)
    Vec.Vadd2(v1, Vec.Vmul(a, dt))
    Vec.Vadd2(r1, Vec.Vmul(v1, dt))
    ellipse(r1.x, r1.y, tank1.radius, tank1.radius)
    
    if (r1.x >= tank2.x - tank1.radius and r1.x <= tank2.x+40+tank1.radius and r1.y <= -670+tank1.radius):
        dt = 0
        tank2.set_turn(tank2.turn + 1)
        counter1 = 0
        tank1.set_fire(False)
        if (Vec.Vmag(v1) >= 60):
            tank2.set_fuel(tank2.fuel - 40)
        elif (Vec.Vmag(v1) >= 50):
            tank2.set_fuel(tank2.fuel - 20)
        elif(Vec.Vmag(v1) >= 40):
            tank2.set_fuel(tank2.fuel - 10)
        else:
            tank2.set_fuel(tank2.fuel - 5)
            
    elif (r1.y <= -700):
        tank2.set_turn(tank2.turn + 1)
        dt = 0
        counter1 = 0
        tank1.set_fire(False)
        
    elif(r1.x >= tower.x-tank1.radius and r1.x <= tower.x+tower.w-tank1.radius and r1.y <= tower.y+tower.h+tank1.radius):
        tank2.set_turn(tank2.turn + 1)
        dt = 0
        counter1 = 0
        tank1.set_fire(False)
        
    elif (r1.x >= bird1.posx - tank1.radius and r1.x <= bird1.posx + 30 + tank1.radius and r1.y >= bird1.posy - tank1.radius and r1.y <= bird1.posy+10+tank1.radius):
        dt = 0
        tank2.set_turn(tank2.turn + 1)
        counter1 = 0
        tank1.set_fire(False)
        bird1.set_posx(-50)
        bird1.set_velx(0)
        
    elif (r1.x >= bird2.posx-tank1.radius and r1.x <= bird2.posx + 30 + tank1.radius and r1.y >= bird2.posy-tank1.radius and r1.y <= bird2.posy+10+tank1.radius):
        dt = 0
        tank2.set_turn(tank2.turn + 1)
        counter1 = 0
        tank1.set_fire(False)
        bird2.set_posx(-50)
        bird2.set_velx(0)
        
    elif (r1.x >= bird3.posx-tank1.radius and r1.x <= bird3.posx + 30 + tank1.radius and r1.y >= bird3.posy-tank1.radius and r1.y <= bird3.posy+10+tank1.radius):
        dt = 0
        tank2.set_turn(tank2.turn + 1)
        counter1 = 0
        tank1.set_fire(False)
        bird3.set_posx(-50)
        bird3.set_velx(0)
        
    elif (r1.x >= power1.posx - tank1.radius and r1.x <= power1.posx + 15 + tank1.radius and r1.y <= power1.posy + tank1.radius and r1.y >= power1.posy - 15 - tank1.radius and powerUp == True):
        tank1.set_fuel(tank1.fuel + 20)
        powerUp = False
    
    elif (r1.x >= power2.posx - tank1.radius and r1.x <= power2.posx + 15 + tank1.radius and r1.y <= power2.posy + tank1.radius and r1.y >= power2.posy - 15 - tank1.radius and powerUp == True):
        tank1.set_radius(tank1.radius + 3)
        powerUp = False
     
    elif (r1.x >= power3.posx - tank1.radius and r1.x <= power3.posx + 15 + tank1.radius and r1.y <= power3.posy + tank1.radius and r1.y >= power3.posy - 15 - tank1.radius and powerUp == True):
        tank1.set_radius(tank1.radius - 3)
        powerUp = False
        print("hi", tank1.radius)
        
    
#birds
def birdy(bird):
    dt = 0.1
    bird.set_posx(bird.posx + (bird.velx * dt))
    if (bird.posx >= 1200):
        bird.velx *= -1
    if (bird.posx <= 0):
        bird.velx *= -1
        
#wind
def windy1(w1, cloud, start):
    dt = 0.1
    Vec.Vadd2(cloud, Vec.Vmul(w1, dt))
    fill(255)
    stroke(255)
    ellipse(cloud.x, -cloud.y, 20, 20)
    ellipse(cloud.x + 15, -cloud.y + 8, 20, 20)
    ellipse(cloud.x + 30, -cloud.y + 16, 20, 20)
    ellipse(cloud.x + 2 , -cloud.y + 20, 20, 20)
    ellipse(cloud.x + 15, -cloud.y + 27, 20, 20)
    if (cloud.x <= 0 or cloud.x >= 1200):
        cloud.x = start
        cloud.y = 200
    stroke(0)
    

    
        
