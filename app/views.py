from django.shortcuts import render, redirect
from django.http import HttpResponse

import urllib.parse 
from urllib.parse import parse_qs

from time import gmtime, strftime

from django.conf import settings

import base64

import requests


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
def spotifyLogin(request):
    scopes = 'user-modify-playback-state streaming user-read-private user-read-email'
    return redirect('https://accounts.spotify.com/authorize' +
      '?response_type=code' +
      '&client_id=' + settings.SPOTIFY_CLIENT_ID +
      '&scope=' + urllib.parse.quote(scopes) +
      '&redirect_uri=' + 'http://127.0.0.1:8000/spotify')

def spotify(request):
    """ Ophalen van de usercode uit de url """
    code = request.GET.get('code')

    """ 'USER_ID : USER_SECRET' in een BASE64 Encoder steken """
    client_id = settings.SPOTIFY_CLIENT_ID
    client_secret = settings.SPOTIFY_CLIENT_SECRET
    message = client_id + ':' + client_secret
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')

    """ Redirect uri instellen """
    redirect_uri = 'http://127.0.0.1:8000/spotify'

    headers = {
        'Authorization': 'Basic ' + base64_message,
    }

    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri
    }

    response = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)

    if response.status_code == 200:
        response_Json = response.json()
        access_token = response_Json['access_token']
        headers = { 'Authorization': 'Bearer ' + access_token }

        """ tracks ophalen met een spotify api endpoint """
        # A Track
        spotify_response = requests.get('https://api.spotify.com/v1/audio-features/1GOdrG8p7TBawr3rEOqT1l?si=BJFUq5waQ6aUvFO0tEIHHw', headers=headers)
       
        # An Album
        #spotify_response = requests.get('https://api.spotify.com/v1/albums/6hQq4WpbUXuoDf3mGJR8qr/tracks', headers=headers)

        spotify_response_Json = spotify_response.json()

        # good ass documentation
        # https://stmorse.github.io/journal/spotify-api.html
        context = {
            'spotify_response': spotify_response_Json
        }
        return render(request, 'template/spotify.html', {'context': context})

    elif response.status_code == 400:
       return render(request, 'template/index.html')
    

  
""" YOUTUBE """
def youtube(request):
    return HttpResponse('youtube')


""" SNAKE """
def snake(request):
    return HttpResponse('snake')


