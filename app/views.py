from django.shortcuts import render
from django.http import HttpResponse

from time import gmtime, strftime


""" HOMEPAGE """
def index(request):
    """ Getting the Time of the day """
    showtime = strftime("%H:%M:%S", gmtime())

    context = {
        'date': showtime 
    }
    return render(request, 'template/index.html', {'context': context})


""" NETFLIX """
def netflix(request):
    return HttpResponse('netflix')


""" SPOTIFY """
def spotify(request):
    return HttpResponse('spotify')


""" YOUTUBE """
def youtube(request):
    return HttpResponse('youtube')


""" SNAKE """
def snake(request):
    return HttpResponse('snake')
