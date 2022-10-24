from django.shortcuts import render
from .forms import SignUpForm

def home(request):
    response = render(request, 'home.html')
    return response


def sign_up(request):
    form=SignUpForm()
    response = render(request, 'sign_up.html', {'form': form})
    return response
