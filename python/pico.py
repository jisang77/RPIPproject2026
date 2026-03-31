from time import sleep
from machine import Pin

#create LED object from pin2,Set Pin2 to output
led=Pin(5,Pin.OUT)
led2=Pin(9,Pin.OUT)
A = input()

if A == '1':
    led.value(1)
    sleep(1)
if A == '2':
    led2.value(1)
    sleep(1)
if A == '3':
    led.value(1)
    led2.value(1)
    sleep(1)
if A == '0':
    led.value(0)
    led2.value(0)



