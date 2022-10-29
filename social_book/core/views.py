from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')



#from: https://www.youtube.com/watch?v=xSUm6iMtREA