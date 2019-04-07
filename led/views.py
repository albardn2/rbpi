from django.shortcuts import render
from gpiozero import LED
from django.shortcuts import redirect
import time
import pigpio
from gpiozero.pins.pigpio import PiGPIOFactory





def home(request):

    return render(request, 'home.html')

def turnon(request):
    # factory = PiGPIOFactory(host='127.0.0.1')
    led = LED(17)
    led.on()
    print('ONNNN')
    return redirect('home')


def turnoff(request):
    # factory = PiGPIOFactory(host='127.0.0.1')
    led = LED(17)
    led.off()
    print('OFFFF')
    return redirect('home')
