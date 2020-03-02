import picamera
from time import sleep

cam = picamera.PiCamera()

cam.start_preview()

#Display Text On Image
cam.annotate_text="Hello!!! Welcome From BLue Jay's Service"

#FLip camera Horizontally TRUE/FALSE
#cam.hflip = True
#cam.vflip = True 

sleep(5)
cam.camputre('image.jpg')

for i in range(5):
	sleep(3)
	cam.capture('/home/pi/camera/pic%s.jpg'%i)

cam.stop_preview() 


