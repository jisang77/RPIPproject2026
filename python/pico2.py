from machine import Pin
import time

#create LED object from pin2,Set Pin2 to output
led=Pin(3,Pin.OUT)
button_pin = Pin(7, Pin.IN, Pin.PULL_UP)

flag=0
while True:
    if (button_pin.value() == 0 and flag == 0):
        print("button on")
        led.value(1)
        time_sleep(0.2)
        flag = 1
    if (button_pin.value() == 0 and flag == 1):
        print("button off")
        led.value(0)
        time_sleep(0.2)
        flag = 0
    time_sleep(0.05)

#4주차 집가기 문제 pico 사용.