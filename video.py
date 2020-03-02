import picamera 
from time import sleep

#Set Up Camera 
cam = picamera.PiCamera()

#Sart Camera 
cam.start_preview()

#Text to Display when taking the video 
cam.annotate_text = 'Hello!!Welcome From BLue Jay Servie'

#Start Recording the Video 
for i in range(40):
	cam.start_recording('/home/pi/Desktop/camera/video%s.h264'% i) #Directary to record the video with the location of poython code 
	sleep(60)

#Stop Recording the Video
cam.stop_recording()

#When it stops, review the record 
cam.stop_preview()
