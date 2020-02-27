import sys
import Adafruit_DHT
import time
import requests 

while True:
	
	humidity, temperature = Adafruit_DHT.read_retry(11,4)

	print 'TEMP: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature, humidity)

	time.sleep(1) 
	
	
	url = 'https://abigailkwan.000webhostapp.com/index.php'
	humid = '{:0.1f}'.format(humidity)
	temp = '{:0.1f}'.format(temperature)

	params = {'temperature': temp, 'humidity': humid}

	x = requests.post(url,params)
	print(x.text)
 

