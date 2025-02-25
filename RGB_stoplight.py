import RPi.GPIO as GPIO
from time import sleep

red = 12
green = 16
blue = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)

while True:
    GPIO.output(green,GPIO.HIGH)
    sleep(5)
    GPIO.output(green,GPIO.LOW)

    GPIO.output(green,GPIO.HIGH)
    GPIO.output(red,GPIO.HIGH)
    sleep(1)
    GPIO.output(green,GPIO.LOW)
    GPIO.output(red,GPIO.LOW)

    GPIO.output(red,GPIO.HIGH)
    sleep(4)
    GPIO.output(red,GPIO.LOW)

GPIO.cleanup()
