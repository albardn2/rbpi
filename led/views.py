from django.shortcuts import render
from gpiozero import LED
from django.shortcuts import redirect
import time




def home(request):

    return render(request, 'home.html')

def turnon(request):
    led = LED(17)
    led.on()
    time.sleep(4)
    print('ONNNN')
    return redirect('home')


def turnoff(request):
    led = LED(17)
    led.off()
    print('OFFFF')
    return redirect('home')
