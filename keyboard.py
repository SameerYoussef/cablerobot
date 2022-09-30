from getch import getch
import turtle
import datetime
import math
import time

screen = turtle.Screen()
screen.title('Keyboard mover')
screen.bgcolor('sky blue')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.tracer(0,0)


angle = 45
length = 200
height = 40

t = turtle.Turtle()


while True:
    char = getch() #read the pressed key
    

    if char == chr(27):
        break
    elif(char==chr(49)):
        angle -= 1
        print(f"reducing angle to {angle}")
    elif(char==chr(55)):
        angle += 1
        print(f"increasing angle to {angle}")
    elif(char==chr(50)):
        length -= 1
        print(f"reducing length to {length}")
    elif(char==chr(56)):
        length += 1
        print(f"increasing length to {length}")
    elif(char==chr(51)):
        height -= 1
        print(f"reducing height to {height}")
    elif(char==chr(57)):
        height += 1
        print(f"increasing height to {height}")
    
    t.clear()
    t.write(f"{angle}/{length}/{height}", font=("Arial", 16, "normal"))
    time.sleep(2)
    