from ursina import *

app = Ursina()

platform = Entity(model="cube", color=color.green, scale = (10,1,10),position = (0,0,0))
cube1 = Entity(model="cube", color=color.blue, scale = (2,0.5,0.5), position = (0,1,-4.5))
cube2 = Entity(model="cube", color=color.red, scale = (2,0.5,0.5), position = (0,1,4.5))
ball = Entity(model="cube", color=color.white, scale = 0.5, position = (0,1,0))
dx = 0
dz = 0.1

camera.position = (0,10,-20)
camera.rotation_x = 30

def update():
	global dx,dz
	if held_keys['right arrow'] and cube1.x < 3.2:
		cube1.x += 0.1
	if held_keys['left arrow'] and cube1.x > -3.2:
		cube1.x -= 0.1
	ball.position = (ball.x-dx,1,ball.z-dz)
	hit_info = ball.intersects()
	if distance(ball,cube1) < 2:
		dx = (ball.x-cube1.x)/10
		dx *= -1
		dz *= -1
		ball.z = ball.z + 0.2
	if distance(ball,cube2) < 2:
		dx = (cube2.x-ball.x)/10
		dx *= -1
		dz *= -1
		ball.z = ball.z - 0.2
	if ball.x < cube2.x and cube2.x > -3.2:
		cube2.x -= 0.05
	if ball.x > cube2.x and cube2.x < 3.2:
		cube2.x += 0.05
	if ball.x > 3.5 or ball.x < -3.5:
		dx *= -1
	if ball.z > 4.1 or ball.z < -4.1:
		ball.position = (0,1,0)
		dx = 0
		dz = 0.1

app.run()