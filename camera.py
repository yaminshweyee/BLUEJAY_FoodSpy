import sys
import picamera
from time import sleep
import requests as req 

cam = picamera.PiCamera()

while True:
#Set up the camera 
#	camera.resoultion = (1280,720)

#Start the Camera 
	cam.start_preview()

#Display Text On Image
	cam.annotate_text="Hello!!! Welcome From BLue Jay's Service"

#FLip camera Horizontally TRUE/FALSE
#cam.hflip = True
#cam.vflip = True 


	cam.capture('/home/pi/Desktop/camera/abby.jpg')
	
	sleep(5)
#for i in range(5):
	#Directory where you wish to capture the pictures 
#	cam.capture('/home/pi/Desktop/camera/pic%s.jpg'%i)
#	sleep(3) #Capture within 15 sec  

#Done after it is capturing the picture 
#cam.stop_preview() 

	url = 'https://abigailkwan.000webhostapp.com/upload_img.php'

	with open('abby.jpg','rb') as f:
		files = {'file' : f}

		r = req.post(url, files = files)
		print(r.text)

	cam.stop_preview()

	#sleep(30)
