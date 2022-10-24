from getch import getche
import turtle
import time
import triangle
import math
import os
from dotenv import load_dotenv
from divider import spread
import threading
import driver
import json

load_dotenv()

steps = int(os.environ.get('STEPS_PER_ROTATION'))
circumference = int(os.environ.get('SPOOL_CIRCUMFERENCE'))

motor_bl = driver.Driver(json.loads(os.environ.get('MOTOR_1_PINS')))
motor_tl = driver.Driver(json.loads(os.environ.get('MOTOR_2_PINS')))
motor_tr = driver.Driver(json.loads(os.environ.get('MOTOR_3_PINS')))
motor_br = driver.Driver(json.loads(os.environ.get('MOTOR_4_PINS')))
motors = [motor_bl, motor_tl, motor_tr, motor_br]

# garden dimensions (mm)
w = 435
h = 225

# Bottom-left motor's initial state
angle = 45
length = 200
drop = 40

screen = turtle.Screen()
screen.title('Keyboard coordinator')
screen.bgcolor('sky blue')
screen.setup(w + 200, h + 200, 1000)
screen.tracer(0,0)

def read_input(text_t, coordinator):
    global angle
    global length
    global drop
    
    # starting lengths
    orig_bl, orig_tl, orig_tr, orig_br = coordinator.coordinate(angle, length, drop)
    
    try:
        while True:
            char = getche() # read the pressed key
            coordinator.clear()
            
            if char == chr(27):
                break
            elif(char==chr(49)):
                angle -= 1            
                print(f"reducing angle to {angle}")
            elif(char==chr(55)):
                angle += 1
                print(f"increasing angle to {angle}")
            elif(char==chr(50)):
                length -= 5
                print(f"reducing length to {length}")
            elif(char==chr(56)):
                length += 5
                print(f"increasing length to {length}")
            elif(char==chr(51)):
                drop -= 5
                print(f"reducing height to {drop}")
            elif(char==chr(57)):
                drop += 5
                print(f"increasing height to {drop}")
            
            bl, tl, tr, br = coordinator.coordinate(angle, length, drop)
            
            text_t.clear()
            text_t.reset()
            text_t.up()
            font = ("Arial", 16, "normal")
            text_t.goto(-200, -200)
            text_t.write(f"{angle}/{length}/{drop}", font=font)
            text_t.goto(-100, 180)
            text_t.write(f"bl: {'%.2f' % bl}, tl: {'%.2f' % tl}, tr: {'%.2f' % tr}, br: {'%.2f' % br}", font=font)
            screen.update()
            
            adjust([orig_bl - bl, orig_tl - tl, orig_tr - tr, orig_br - br])
            orig_bl = bl
            orig_tl = tl
            orig_tr = tr
            orig_br = br
            
    except KeyboardInterrupt:
        for motor in motors:
            motor.cleanup()
        driver.gpio_cleanup()
        exit(1)

def adjust(deltas):
    directions = [delta > 0 for delta in deltas] # False - Up - Counterclockwise
    all_steps = [math.floor(abs(delta)/circumference * steps) for delta in deltas]
    longest = max(all_steps)
        
    for motor in range(4):
        threading.Thread(target=motors[motor].drive, args=(spread(longest, all_steps[motor]), directions[motor])).start()

    time.sleep(float(os.environ.get('STEP_SLEEP')) * longest)

if __name__ == "__main__":
    triangle.draw_outline(w, h, turtle.Turtle())
    coordinator = triangle.Triangle(w, h, turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle())
    coordinator.coordinate(angle, length, drop)
    screen.update()
    read_input(turtle.Turtle(), coordinator)
    input("Press ENTER to end...")
