from django.shortcuts import render
import requests

def gpt3(request):
    return render(request, 'gpt3.html', {})