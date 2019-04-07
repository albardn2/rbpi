from django.shortcuts import render
from gpiozero import LED
from django.shortcuts import redirect
import time
import pigpio




def home(request):

    return render(request, 'home.html')

def turnon(request):
    pi1 = pigpio.pi()
    pi1.write(17, 1)
    # led = LED(17)
    # led.on()
    print('ONNNN')
    return redirect('home')


def turnoff(request):
    pi1 = pigpio.pi()
    pi1.write(17, 0)
    # led = LED(17)
    # led.off()
    print('OFFFF')
    return redirect('home')
