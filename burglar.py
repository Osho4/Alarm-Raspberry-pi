import RPi.GPIO as GPIO
import time

sensor = 18
buzzer = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)
print "IR Sensor Ready....."
print " "

try: 
   while True:
      if GPIO.input(sensor):
          GPIO.output(buzzer,True)
          print "Object Detected"
          while GPIO.input(sensor):
              time.sleep(0.2)
      else:
          GPIO.output(buzzer,False)


except KeyboardInterrupt:
    GPIO.cleanup()
