import picamera
from time import sleep


#Set up the camera 
cam = picamera.PiCamera()

#Start the Camera 
cam.start_preview()

#Display Text On Image
cam.annotate_text="Hello!!! Welcome From BLue Jay's Service"

#FLip camera Horizontally TRUE/FALSE
#cam.hflip = True
#cam.vflip = True 

sleep(3)
cam.capture('image.jpg')

for i in range(5):
	sleep(2)
	#Directory where you wish to capture the pictures 
	cam.capture('/home/pi/Desktop/camera/pic%s.jpg'%i)
 
#Done after it is capturing the picture 
cam.stop_preview() 


