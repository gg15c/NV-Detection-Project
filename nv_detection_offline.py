# this is hampton.
# import Nvidia utility
import jetson.inference
import jetson.utils

import argparse
import sys

import RPi.GPIO as GPIO
import time


# for 1st Motor on the board

# this is right wheel
IN1 = 37
IN2 = 35
PWM1 = 32

# this is left wheel
IN3 = 31
IN4 = 29
PWM2 = 33


def main(): #define a PWM function to control GPIO
	
	if detection.ClassID == 1:
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
		p1.start(30) # the 10 equals the duty cycle
		p2.start(30)

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
		time.sleep(5)

		# Stop
		GPIO.output(IN1, GPIO.LOW)
		GPIO.output(IN2, GPIO.LOW)
		GPIO.output(IN3, GPIO.LOW)
		GPIO.output(IN4, GPIO.LOW)
		time.sleep(1)

		# Backward
		#GPIO.output(IN1, GPIO.LOW)
		#GPIO.output(IN2, GPIO.HIGH)
		#GPIO.output(IN3, GPIO.HIGH)
		#GPIO.output(IN4, GPIO.LOW)
		#time.sleep(5)


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



# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.", 
						   formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage())

parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use") 

#configure camera (for CSI default="0", USB camera = default="/dev/video0")
parser.add_argument("--camera", type=str, default="/dev/video0", help="index of the MIPI CSI camera to use (e.g. CSI camera 0)\nor for VL42 cameras, the /dev/video device to use.\nby default, MIPI CSI camera 0 will be used.")
parser.add_argument("--width", type=int, default=1280, help="desired width of camera stream (default is 1280 pixels)")
parser.add_argument("--height", type=int, default=720, help="desired height of camera stream (default is 720 pixels)")

try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)

# load the object detection network
net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)

# create the camera and display
camera = jetson.utils.gstCamera(opt.width, opt.height, opt.camera)
#display = jetson.utils.glDisplay()

# process frames until user exits
while True:
	# capture the image
	img, width, height = camera.CaptureRGBA()

	# detect objects in the image (with overlay)
	detections = net.Detect(img, width, height, opt.overlay)

	# print the detections
	print("detected {:d} objects in image".format(len(detections)))

	for detection in detections:
		print(net.GetClassDesc(detection.ClassID)) # this will give you a ture index by mapping the number.
		print(detection.ClassID) # this will only give a classID number.
		print(detection)
	
		#if detection.ClassID == 1:
		main()

	# render the image
	#display.RenderOnce(img, width, height)

	# update the title bar
	#display.SetTitle("{:s} | Network {:.0f} FPS".format(opt.network, net.GetNetworkFPS()))

	# print out performance info
	net.PrintProfilerTimes()
