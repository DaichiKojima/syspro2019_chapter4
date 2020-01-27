
import time
import RPi.GPIO as GPIO
def setservo(deg):
   servo.ChangeDutyCycle(2.5 + 9.5 * ( deg + 90) / 180 )

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
@@ -12,12 +14,15 @@

for i in range(5):
	servo.ChangeDutyCycle(bottom)
        setservo(-90)
	time.sleep(1.0)

	servo.ChangeDutyCycle(middle)
        setservo(0)
	time.sleep(1.0)

	servo.ChangeDutyCycle(top)
        setservo(90)
	time.sleep(1.0)



