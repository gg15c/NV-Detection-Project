# this is hampton.
# import Nvidia utility
import jetson.inference
import jetson.utils

import argparse
import sys

import RPi.GPIO as GPIO
import time


output_pin1 = 32 #GPIO number
output_pin2 = 33 


def main(): #define a PWM function to control GPIO
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(output_pin1, GPIO.OUT, initial=GPIO.HIGH)
	p1 = GPIO.PWM(output_pin1, 50)
	GPIO.setup(output_pin2, GPIO.OUT, initial=GPIO.HIGH)
	p2 = GPIO.PWM(output_pin2, 50)

	print("PWM running. Press CTRL+C to exit.")
	try:
		if detection.ClassID == 1:
			#p1.start(2.5)
			#print("p1 start at 2.5%")
			#time.sleep(1)
			p2.start(2.5)
			print("p2 start at 2.5%")
			time.sleep(0.25)
			#p1.start(7.25)
			#print("p1 start at 7.25%")
			#time.sleep(1)
			#p2.start(7.25)
			#print("p2 start at 7.25%")
			#time.sleep(0.5)
			#p1.start(12)
			#print("p1 start at 12%")
			#time.sleep(1)
			p2.start(12)
			print("p2 start at 12%")
			time.sleep(0.25)
			#p1.start(7.25)
			#print("p1 start at 7.25%")
			#time.sleep(1)
			#p2.start(2.5)
			#print("p2 start at 2.5%")
			#time.sleep(1)

	finally:
		p1.stop()
		p2.stop()
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
display = jetson.utils.glDisplay()

# process frames until user exits
while display.IsOpen():
	# capture the image
	img, width, height = camera.CaptureRGBA()

	# detect objects in the image (with overlay)
	detections = net.Detect(img, width, height, opt.overlay)

	# print the detections
	print("detected {:d} objects in image".format(len(detections)))

	for detection in detections:
		print(net.GetClassDesc(detection.ClassID)) # this will give you a ture index by mapping the number.
		print(detection.ClassID) # this will only give a classID number.
		
		#if detection.ClassID == 1:
		main()

	# render the image
	display.RenderOnce(img, width, height)

	# update the title bar
	display.SetTitle("{:s} | Network {:.0f} FPS".format(opt.network, net.GetNetworkFPS()))

	# print out performance info
	net.PrintProfilerTimes()
