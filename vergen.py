import turtle
import random

pencere = turtle.Screen()
pencere.screensize(600, 600)
pencere.title('kapluğumbaları yakala')
pencere.bgcolor('blue')

oyuncu = turtle.Turtle()
oyuncu.color('red')
oyuncu.shape('square')
oyuncu.shapesize(3)
oyuncu.penup()

speed = 1

def soladon():
    oyuncu.left(30)

def sagadon():
    oyuncu.right(30)

def hızıartir():
    global speed
    speed = speed + 1

def hızıazalt():
    global speed
    speed = speed - 1



pencere.listen()
pencere.onkey(soladon,'Left')
pencere.onkey(sagadon,'Right')
pencere.onkey(hızıartir,'Up')
pencere.onkey(hızıazalt,'Down')

maxhedef = 5
hedefler = []
for i in range(maxhedef): 

    hedefler.append(turtle.Turtle())
    hedefler[i].penup()
    hedefler[i].color('white')
    hedefler[i].shape()
    hedefler[i].speed(0)
    hedefler[i].setposition(random.randint(-300, 300),random.randint(-300, 300))


while True:
    oyuncu.forward(speed)



    if oyuncu.xcor() > 300 or oyuncu.xcor() < -300:
        oyuncu.right(180)
    if oyuncu.ycor() > 300 or oyuncu.ycor() < -300:
        oyuncu.right(180)    

    for i in range(maxhedef):
        hedefler[i].forward(1)
    
    if oyuncu.distance(hedefler[i]) < 40:
        hedefler[i].setposition(random.randint(-300, 300),random.randint(-300, 300))
