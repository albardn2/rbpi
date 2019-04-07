from django.shortcuts import render
from gpiozero import LED
from django.shortcuts import redirect
import time
import pigpio




def home(request):

    return render(request, 'home.html')

def turnon(request):
    factory = PiGPIOFactory(host='127.0.0.1')
    led = LED(17, pin_factory=factory)
    led.on()
    print('ONNNN')
    return redirect('home')


def turnoff(request):
    factory = PiGPIOFactory(host='127.0.0.1')
    led = LED(17, pin_factory=factory)
    led.off()
    print('OFFFF')
    return redirect('home')
