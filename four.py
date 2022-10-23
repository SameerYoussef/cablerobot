#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

# Each motor occupies 4 pins on the RPi
m1_motor_pins = [17, 18, 27, 22]
m2_motor_pins = [4, 23, 24, 25]
m3_motor_pins = [6, 13, 19, 26]
m4_motor_pins = [12, 16, 20, 21]

step_sleep = 0.0015 # careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_count = 4096 # 5.625*(1/64) per step, 4096 steps is 360°

# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
step_sequence = [[1,0,0,1],
                [1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1]]

def setup():
    GPIO.setmode( GPIO.BCM )
    for motor in [m1_motor_pins, m2_motor_pins, m3_motor_pins, m4_motor_pins]:
        for pin in range(0, len(m1_motor_pins)):
            GPIO.setup(motor[pin], GPIO.OUT)
            GPIO.output(motor[pin], GPIO.LOW)

def drive(m1_steps, m2_steps, m3_steps, m4_steps): # m1_steps = ([F,T,F,T,F], True)
    m1_count = m2_count = m3_count = m4_count = 0
    for steps in [m1_steps, m2_steps, m3_steps, m4_steps]:
        direction = steps[1]
        for steps in steps[0]:
            # need to know which motor we are on
            pass
    
    direction = True # True (Down) for clockwise, False (Up) for counter-clockwise
    motor_step_counter = 0
    for i in range(step_count):
        for pin in range(0, len(m1_motor_pins)):
            GPIO.output(m1_motor_pins[pin], step_sequence[motor_step_counter][pin])
            GPIO.output(m2_motor_pins[pin], step_sequence[motor_step_counter][pin])
            GPIO.output(m3_motor_pins[pin], step_sequence[motor_step_counter][pin])
            GPIO.output(m4_motor_pins[pin], step_sequence[motor_step_counter][pin])
        if direction == True:
            motor_step_counter = (motor_step_counter - 1) % 8
        else:
            motor_step_counter = (motor_step_counter + 1) % 8
        time.sleep(step_sleep)
    cleanup()
    exit(0)

def cleanup():
    for motor in [m1_motor_pins, m2_motor_pins, m3_motor_pins, m4_motor_pins]:
        for pin in range(0, len(m1_motor_pins)):
            GPIO.output(motor[pin], GPIO.LOW)
    GPIO.cleanup()

if __name__ == "__main__":
    # the meat
    try:
        while True:
            i = 0

            # print(f"i is {i} and step_count is {step_count}")
            if i == step_count-1:
                direction = not direction

    except KeyboardInterrupt:
        cleanup()
        exit( 1 )
