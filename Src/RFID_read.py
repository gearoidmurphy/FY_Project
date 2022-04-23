import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

def getTagNumber():
    while True:
        try:
            id,text = reader.read()
            print(text)
            return text
        finally:
	        GPIO.cleanup()
