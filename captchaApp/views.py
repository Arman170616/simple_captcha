from django.shortcuts import render
from .forms import CaptchaForm
from django.contrib import messages

# Create your views here.


def index(request):
    if request.method=="POST":
        form = CaptchaForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Captcha verified successfully')
        else:
            messages.error(request, 'wrong captcha')
    form = CaptchaForm()
    return render(request, 'index.html', {"form":form})
