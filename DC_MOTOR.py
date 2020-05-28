#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# for 1st Motor on ENA
IN1 = 37
IN2 = 35
IN3 = 31
IN4 = 29
PWM1 = 32
PWM2 = 33

# set pin numbers to the board's
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PWM1, GPIO.OUT, initial=GPIO.HIGH)
p1 = GPIO.PWM(PWM1, 50) # the 50 = 50 Hz.
GPIO.setup(PWM2, GPIO.OUT, initial=GPIO.HIGH)
p2 = GPIO.PWM(PWM2, 50)


# initialize 
GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
p1.start(10) # the 10 equals the duty cycle
p2.start(100)

# Stop
#GPIO.output(IN3, GPIO.HIGH)
#GPIO.output(IN1, GPIO.LOW)
#GPIO.output(IN2, GPIO.LOW)
#time.sleep(1)

# Forward
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.HIGH)
time.sleep(3)

# Stop
#GPIO.output(IN1, GPIO.LOW)
#GPIO.output(IN2, GPIO.LOW)
#GPIO.output(IN3, GPIO.LOW)
#GPIO.output(IN4, GPIO.LOW)
#time.sleep(1)

# Backward
#GPIO.output(IN1, GPIO.LOW)
#GPIO.output(IN2, GPIO.HIGH)
#time.sleep(1)

# Stop
#GPIO.output(ENA, GPIO.LOW)
#GPIO.output(IN1, GPIO.LOW)
#GPIO.output(IN2, GPIO.LOW)
#time.sleep(1)

#turn left
#GPIO.output(IN1, GPIO.LOW)
#GPIO.output(IN2, GPIO.HIGH)
#GPIO.output(IN3, GPIO.HIGH)
#GPIO.output(IN4, GPIO.LOW)
#time.sleep(3)


# Stop
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.LOW)
time.sleep(1)


GPIO.cleanup()
