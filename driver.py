#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import os
from dotenv import load_dotenv

# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
step_sequence = [[1,0,0,1],
                [1,0,0,0],
                [1,1,0,0],
                [0,1,0,0],
                [0,1,1,0],
                [0,0,1,0],
                [0,0,1,1],
                [0,0,0,1]]

load_dotenv()

class Driver():
  
  def __init__(self, pins) -> None:
    self.pins = pins
    self.step_sleep = float(os.environ.get('STEP_SLEEP'))
    self.motor_step_counter = 0
    
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
      GPIO.setup(pin, GPIO.OUT)
      GPIO.output(pin, GPIO.LOW)

  def cleanup(self):
    for pin in self.pins:
      GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()

  def drive(self, steps, direction):
    for i in range(steps):
      if steps[i] == True:
        for pin in range(0, len(self.pins)):
          GPIO.output( self.pins[pin], step_sequence[self.motor_step_counter][pin] )
        if direction == True:
          self.motor_step_counter = (self.motor_step_counter - 1) % 8
        else:
          self.motor_step_counter = (self.motor_step_counter + 1) % 8
      time.sleep(self.step_sleep)
