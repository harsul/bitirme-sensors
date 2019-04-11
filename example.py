# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 14:27:38 2019

@author: Harun
"""

from time import sleep
from gpiozero import InputDevice,LightSensor
import Adafruit_DHT
import RPi.GPIO as GPIO

#input 
rain=InputDevice(18)
ldr=LightSensor(4)
dht=Adafruit_DHT.DHT11
soil=21

# Use the GPIO BCM pin numbering scheme.
GPIO.setmode(GPIO.BCM)
# Receive input signals through the pin.
GPIO.setup(soil, GPIO.IN)

def temperature():
    print("Temperature sensor:")
    print("-"*10)
    
    humidity, temperature = Adafruit_DHT.read_retry(dht, 14)
    if humidity is not None and temperature is not None:
        print ("Humidity: {} Temperature: {} ".format(humidity,temperature))
    else:
        print("Failed to read data!!!")
        
    sleep(1)

def rainsensor():
    print("Rain sensor:")
    print("-"*10)
    
    if rain.is_active is not None:
        if not rain.is_active:
            print("Rain Detected")
        else:
            print ("No Rain Detected")
    else:
        print("Failed to read data!!!")
        
    sleep(1)

def ldrsensor():
    print("LDR sensor:")
    print("-"*10)
    
    if ldr.value is not None:
        print (ldr.value)
    else:
        print("Failed to read data!!!")
        
    sleep(1)

def soilmeasure():
    print("Soil sensor:")
    print("-"*10)
    if GPIO.input(soil):
	print("No water detected")	
    else:
	print("Water detected")
			
    sleep(1)
  
try:
    while True:
        rainsensor()
        ldrsensor()
        #temperature()
        soilmeasure()
            
        sleep(10)
        
except KeyboardInterrupt:
    print ("Exit")
    GPIO.cleanup()
    

    
