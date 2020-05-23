import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD) #set GPIO board on the jetson nano
 
# Declaration of the input pin which is connected with the sensor
GPIO_PIN = 15 # setting the number of GPIO
GPIO.setup(GPIO_PIN, GPIO.IN)
 
# Break between the results will be defined here (in seconds)
delayTime = 1
 
print("Sensor-Test [press ctrl+c to end]")
 
# main program loop
try:
        while True:
            if GPIO.input(GPIO_PIN) == True:
                print("LineTracker is on the line")
            else:
                print("LineTracker is not on the line")
            print("---------------------------------------")
 
            # Reset + Delay
            time.sleep(delayTime)
 
finally:
	GPIO.cleanup() # If you press ctrl+c, the system will jump to finally to clean up the register.

