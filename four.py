#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

# M1
m1_in1 = 17
m1_in2 = 18
m1_in3 = 27
m1_in4 = 22

# M2
m2_in1 = 4
m2_in2 = 23
m2_in3 = 24
m2_in4 = 25

# M3
m3_in1 = 6
m3_in2 = 13
m3_in3 = 19
m3_in4 = 26

# M4
m4_in1 = 12
m4_in2 = 16
m4_in3 = 20
m4_in4 = 21

# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.0015

step_count = int(4096*0.3) # 5.625*(1/64) per step, 4096 steps is 360°

direction = True # True (Down) for clockwise, False (Up) for counter-clockwise

# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]

# setting up
GPIO.setmode( GPIO.BCM )
GPIO.setup( m1_in1, GPIO.OUT )
GPIO.setup( m1_in2, GPIO.OUT )
GPIO.setup( m1_in3, GPIO.OUT )
GPIO.setup( m1_in4, GPIO.OUT )
GPIO.setup( m2_in1, GPIO.OUT )
GPIO.setup( m2_in2, GPIO.OUT )
GPIO.setup( m2_in3, GPIO.OUT )
GPIO.setup( m2_in4, GPIO.OUT )
GPIO.setup( m3_in1, GPIO.OUT )
GPIO.setup( m3_in2, GPIO.OUT )
GPIO.setup( m3_in3, GPIO.OUT )
GPIO.setup( m3_in4, GPIO.OUT )
GPIO.setup( m4_in1, GPIO.OUT )
GPIO.setup( m4_in2, GPIO.OUT )
GPIO.setup( m4_in3, GPIO.OUT )
GPIO.setup( m4_in4, GPIO.OUT )

# initializing
GPIO.output( m1_in1, GPIO.LOW )
GPIO.output( m1_in2, GPIO.LOW )
GPIO.output( m1_in3, GPIO.LOW )
GPIO.output( m1_in4, GPIO.LOW )
GPIO.output( m2_in1, GPIO.LOW )
GPIO.output( m2_in2, GPIO.LOW )
GPIO.output( m2_in3, GPIO.LOW )
GPIO.output( m2_in4, GPIO.LOW )
GPIO.output( m3_in1, GPIO.LOW )
GPIO.output( m3_in2, GPIO.LOW )
GPIO.output( m3_in3, GPIO.LOW )
GPIO.output( m3_in4, GPIO.LOW )
GPIO.output( m4_in1, GPIO.LOW )
GPIO.output( m4_in2, GPIO.LOW )
GPIO.output( m4_in3, GPIO.LOW )
GPIO.output( m4_in4, GPIO.LOW )


m1_motor_pins = [m1_in1,m1_in2,m1_in3,m1_in4]
m2_motor_pins = [m2_in1,m2_in2,m2_in3,m2_in4]
m3_motor_pins = [m3_in1,m3_in2,m3_in3,m3_in4]
m4_motor_pins = [m4_in1,m4_in2,m4_in3,m4_in4]
motor_step_counter = 0 ;


def cleanup():
    GPIO.output( m1_in1, GPIO.LOW )
    GPIO.output( m1_in2, GPIO.LOW )
    GPIO.output( m1_in3, GPIO.LOW )
    GPIO.output( m1_in4, GPIO.LOW )
    GPIO.output( m2_in1, GPIO.LOW )
    GPIO.output( m2_in2, GPIO.LOW )
    GPIO.output( m2_in3, GPIO.LOW )
    GPIO.output( m2_in4, GPIO.LOW )
    GPIO.output( m3_in1, GPIO.LOW )
    GPIO.output( m3_in2, GPIO.LOW )
    GPIO.output( m3_in3, GPIO.LOW )
    GPIO.output( m3_in4, GPIO.LOW )
    GPIO.output( m4_in1, GPIO.LOW )
    GPIO.output( m4_in2, GPIO.LOW )
    GPIO.output( m4_in3, GPIO.LOW )
    GPIO.output( m4_in4, GPIO.LOW )
    GPIO.cleanup()


# the meat
try:
    while True:
        i = 0
        for i in range(step_count):
            for pin in range(0, len(m1_motor_pins)):
                GPIO.output( m1_motor_pins[pin], step_sequence[motor_step_counter][pin] )
                GPIO.output( m2_motor_pins[pin], step_sequence[motor_step_counter][pin] )
                GPIO.output( m3_motor_pins[pin], step_sequence[motor_step_counter][pin] )
                GPIO.output( m4_motor_pins[pin], step_sequence[motor_step_counter][pin] )
            if direction==True:
                motor_step_counter = (motor_step_counter - 1) % 8
            elif direction==False:
                motor_step_counter = (motor_step_counter + 1) % 8
            else: # defensive programming
                print( "uh oh... direction should *always* be either True or False" )
                cleanup()
                exit( 1 )
            time.sleep( step_sleep )
        # print(f"i is {i} and step_count is {step_count}")
        if i == step_count-1:
            direction = not direction

except KeyboardInterrupt:
    cleanup()
    exit( 1 )

cleanup()
exit( 0 )



