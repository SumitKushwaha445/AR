
from django.shortcuts import render

# Create your views here.

def start_page_action(request):
    return render (request, 'start_page.html')