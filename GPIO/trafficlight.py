from gpiozero import Button, TrafficLights, Buzzer  
from time import sleep  
  
buzzer = Buzzer(15)  
button = Button(21)  
lights = TrafficLights(25, 8, 7)  
  
while True:  
	button.wait_for_press() 
	buzzer.on() 
	#lights.green.on()  
	#sleep(5)  
	#lights.green.off()
	#lights.amber.on()  
	#sleep(1)  
	#lights.amber.off()
	#lights.red.on()  
	#sleep(6)  
	#lights.red.off()
	#lights.off() 
	#buzzer.off()
	   
	lights.red.on()  
	sleep(7)  
	lights.red.off()
	lights.amber.on()  
	sleep(1)  
	lights.amber.off()
	lights.green.on()  
	sleep(5)  
	lights.green.off()
	lights.off() 
	buzzer.off()

