import imp
from xmlrpc.client import Boolean
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import talent
import sys
sys.path.append('../')
from Translator import textGenerator
import environ
from django.db.utils import IntegrityError

env = environ.Env()
environ.Env.read_env()

def home(request):
    return render(request, 'home.html')


def writerPage(request):
    return render(request, 'writer.html')

def scriptPage(request):
    userLength = int(request.GET.get('length'))
    inputText = request.GET.get('textDescription')
    userTemperature = float(request.GET.get('userTemperature'))
    generatedText = textGenerator(inputText, userTemperature, userLength)
    return render(request, 'writer.html',{'generatedText':generatedText, 'userText':inputText, 'userTemperature':userTemperature})

def wordCounter(request):
    userText = request.GET.get('userText')
    if userText is not None:
        wordCount = len(userText.split())
    else:
        wordCount = 0
    return render(request, 'counter.html',{'wordCount':wordCount, 'userText':userText})

def calculator(request):
    try:
        speed = int(request.GET.get('speed'))
        words = int(request.GET.get('words'))
    except:
        speed = 157
        words = 0
    minuts = int(words/speed)
    seconds = int(((words/speed) - minuts) * 60)
    print(minuts,':', seconds)
    return render(request, 'calculator.html',{'minuts':minuts, 'seconds':seconds})

def talents(request):
    try:
        newTalent = talent()
        newTalent.fullName = request.POST.get('fullName')
        newTalent.description = request.POST.get('description')
        # newTalent.photo = request.FILES['photo']
        newTalent.birtdate = request.POST.get('birtday')
        newTalent.facebook = request.POST.get('facebook')
        newTalent.instagram = request.POST.get('instagram')
        newTalent.youtube = request.POST.get('youtube')
        newTalent.phoneNumber = request.POST.get('phoneNumber')
        newTalent.email = request.POST.get('email')
        newTalent.country = request.POST.get('country')
        newTalent.state = request.POST.get('state')
        newTalent.city = request.POST.get('city')
        newTalent.gender = request.POST.get('gender')
        newTalent.actor = Boolean(request.POST.get('actor'))
        newTalent.announcer = Boolean(request.POST.get('announcer'))
        newTalent.singer = Boolean(request.POST.get('singer'))
        newTalent.dancer = Boolean(request.POST.get('dancer'))
        newTalent.writer = Boolean(request.POST.get('writer'))
        newTalent.photographer = Boolean(request.POST.get('photographer'))
        newTalent.save()
    except(IntegrityError):
        return render(request, 'register.html',{'error':'This phone number is already registered'})

   

    return HttpResponseRedirect('/')


def register(request):
    return render(request, 'register.html')
