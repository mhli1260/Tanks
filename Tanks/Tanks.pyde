from PhysicsEngine import*
# from Shooter import*
from Tank import*
shift = 20

def setup():
    size(1200,1200)

#changing angle, velocity, and position
def keyPressed():
    global fire, turn
    if (tank2.turn % 2 == 0):
        if (key == 'q'):
            tank2.set_angle(tank2.shooterangle+5)
        if (key == 'w'):
            tank2.set_angle(tank2.shooterangle-5)
        if (key == 'a'):
            tank2.set_vel(tank2.vel + 5)
        if (key == 's'):
            tank2.set_vel(tank2.vel - 5)
        if (key == 'z' and tank2.x + 60 < tower.x):
            tank2.set_posx(tank2.x - 5)
        if (key == 'x' and tank2.x + 60 < tower.x):
            tank2.set_posx(tank2.x + 5)
    if (tank2.turn % 2 == 1):
        if (key == 'o'):
            tank1.set_angle(tank1.shooterangle + 5)
            print(tank1.shooterangle)
        if (key == 'p'):
            tank1.set_angle(tank1.shooterangle - 5)
        if (key == 'l'):
            tank1.set_vel(tank1.vel - 5)
        if (key == 'k'):
            tank1.set_vel(tank1.vel + 5)
        if (keyCode == LEFT and tank1.x > tower.x + 60):
            tank1.set_posx(tank1.x - 5)
        if (keyCode == RIGHT and tank1.x > tower.x + 60):
            tank1.set_posx(tank1.x + 5)
    if (keyCode ==  32 and tank2.turn % 2 == 0):
        tank2.set_fire(True)
    if (keyCode == 32 and tank2.turn % 2 == 1):
        tank1.set_fire(True)
    
def draw():
    global turn, fire, r2
    #basic background stuff
    scale (1,-1)
    background(255)
    fill(0, 200, 0)
    rect(0, -700, 1200, -400)
    fill(173, 216, 255)
    rect(0, 0, 1200, -700)
    textSize(20)
    fill(0,0,0)
    #changing red tank color based on fuel
    if (tank1.fuel <=100):
        if (tank1.fuel >= 80):
            tank1.set_g(40)
            tank1.set_b(40)
        elif(tank1.fuel >= 60):
            tank1.set_g(90)
            tank1.set_b(90)
        elif(tank1.fuel >= 40):
            tank1.set_g(140)
            tank1.set_b(140)
        elif(tank1.fuel >= 20):
            tank1.set_g(190)
            tank1.set_b(190)
    fill(tank1.r, tank1.g, tank1.b)
    #drawing red tank
    rect(tank1.x, tank1.y+shift, 30, 18)
    quad(tank1.x - 20, tank1.y+shift, tank1.x+50, tank1.y+shift, tank1.x+30, tank1.y, tank1.x, tank1.y)
    circle(tank1.x + 2, tank1.y + 10, 5)
    circle(tank1.x + 15, tank1.y + 10, 5)
    circle(tank1.x + 28, tank1.y + 10, 5)
    #changing blue tank color based on fuel
    if (tank2.fuel <=100):
        if (tank2.fuel >= 80):
            tank2.set_g(40)
            tank2.set_r(40)
        elif(tank2.fuel >= 60):
            tank2.set_g(90)
            tank2.set_r(90)
        elif(tank2.fuel >= 40):
            tank2.set_g(140)
            tank2.set_r(140)
        elif(tank2.fuel >= 20):
            tank2.set_g(190)
            tank2.set_r(190)
    fill(tank2.r,tank2.g,tank2.b)
    #drawing blue tank
    rect(tank2.x, tank2.y+shift, 30, 18)
    quad(tank2.x - 20, tank2.y+shift, tank2.x+50, tank2.y+shift, tank2.x+30, tank2.y, tank2.x, tank2.y)
    circle(tank2.x + 2, tank2.y + 10, 5)
    circle(tank2.x + 15, tank2.y + 10, 5)
    circle(tank2.x + 28, tank2.y + 10, 5)
    #drawing tower
    fill(0,0,0)
    rect(tower.x, tower.y, tower.w, tower.h)
    #drawing shooters
    strokeWeight(2.5)
    line(tank1.x, tank1.y+30, tank1.x - cos(tank1.shooterangle*PI/180)*scl, tank1.y + sin(tank1.shooterangle*PI/180)*scl+30)
    line(tank2.x+30, tank2.y+30, tank2.x + cos(tank2.shooterangle*PI/180)*scl+30, tank2.y + sin(tank2.shooterangle*PI/180)*scl+30)
    #text for fuel and velocity
    scale(1, -1)
    fill(0,0,0)
    text("Vel: ", 20, 27)
    text(tank2.vel, 60, 27)
    text("Vel: ", 1060, 27)
    text(tank1.vel, 1100, 27)
    text("Fuel: ", 20, 50)
    text(tank2.fuel, 70, 50)
    text("Fuel: ", 1060, 50)
    text(tank1.fuel, 1110, 50)
    text("Turn: ", 550, 45)
    #indicating turns
    if(tank2.turn % 2 == 0):
        fill(255, 0, 0)
        text("1", 610, 45)
    if(tank2.turn % 2 == 1):
        fill(255, 0, 0)
        text("2", 610, 45)
    #drawing birds
    scale(1, -1)
    birdy(bird1)
    birdy(bird2)
    birdy(bird3)
    noFill()
    arc(bird1.posx, bird1.posy, 18, 10, 0, PI)
    arc(bird1.posx+15, bird1.posy, 18, 10, 0, PI) 
    # line(bird1.posx, bird1.posy, bird1.posx + 15, bird1.posy)
    arc(bird2.posx, bird2.posy, 18, 10, 0, PI)
    arc(bird2.posx+15, bird2.posy, 18, 10, 0, PI)
    arc(bird3.posx, bird3.posy, 18, 10, 0, PI)
    arc(bird3.posx + 15, bird3.posy, 18, 10, 0, PI)
    fill(0)
    scale(1, -1)
    textSize(15)
    #power ups
    fill(power1.r, power1.g, power1.b)
    rect(power1.posx, -power1.posy, 15, 15)
    rect(20, 70, 15, 15)
    fill(0)
    text("= +20 to fuel", 45, 85)
    fill(power2.r, power2.g, power2.b)
    rect(power2.posx, -power2.posy, 15, 15)
    rect(20, 90, 15, 15)
    fill(0)
    text("= +3 to radius", 45, 105)
    fill(power3.r, power3.g, power3.b)
    rect(20, 110, 15, 15)
    rect(power3.posx, -power3.posy, 15, 15)
    fill(0)
    text("= -3 to radius", 45, 125)
    scale(1,-1)
    #calling projectile/physics code
    if (tank2.fire == True and tank2.turn % 2 == 0):
        move2()
        fill(255, 0, 0)
    if (tank1.fire == True and tank2.turn % 2 == 1):
        move1()
    #clouds
    if (tank2.turn % 2 == 0):
        windy1(w2, cloud4, 100)
        windy1(w2, cloud5, 100)
        windy1(w2, cloud6, 100)
    if (tank2.turn % 2 == 1):
        windy1(w1, cloud1, 1100)
        windy1(w1, cloud2, 1100)
        windy1(w1, cloud3, 1100)
    #game over screen
    if (tank2.fuel <= 0 or tank1.fuel <= 0):
        noLoop()
        background(0,0,0)
        scale(1, -1)
        fill(255, 0, 0)
        textSize(100)
        text("Game Over", 350, 400)
    
  
    
        
  


    

    

    
