from django.shortcuts import render
from gpiozero import LED
from django.shortcuts import redirect
import time
import RPi.GPIO as GPIO




def home(request):

    return render(request, 'home.html')

def turnon(request):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT)
    GPIO.output(17,GPIO.HIGH)
    print('ONNNN')
    return redirect('home')


def turnoff(request):
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(17,GPIO.OUT)
    # GPIO.output(17,GPIO.LOW)
    GPIO.cleanup()
    print('OFFFF')
    return redirect('home')
