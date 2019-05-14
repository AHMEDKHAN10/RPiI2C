import RPi.GPIO as GPIO
import dht11
import time
import datetime



# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()


# read data using pin gpio27
reading = dht11.DHT11(pin=27)

while True:
    result = reading.read()
    if result.is_valid():
        print("temperature and humidity at: " + str(datetime.datetime.now()))
        print("temperature reading: %d C" % result.temperature)
        print("humidity reading: %d %%" % result.humidity)

    time.sleep(1)
