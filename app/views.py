from django.shortcuts import render, redirect
from django.http import HttpResponse

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

import urllib.parse 
from urllib.parse import parse_qs

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
def spotifyLogin(request):
    scopes = 'user-read-private user-read-email'
    return redirect('https://accounts.spotify.com/authorize' +
      '?response_type=code' +
      '&client_id=' + 'ff1a2ba0fcd642fbb63b304eeaf19c90' +
      '&scope=' + urllib.parse.quote(scopes) +
      '&redirect_uri=' + 'http://127.0.0.1:8000/spotify')

def spotify(request):
    """ 1. Ophalen van de code uit de url """
    code = request.GET.get('code');

    """ 2. code invullen in onderstaand commando """
    """ 3. 'USER_ID : USER_SECRET' in een BASE64 Encoder steken en meegeven in onderstaand commazndo """
    """ 3. Redirect url instellen op onze url """
    """ curl -H "Authorization: Basic $BASE64-DATA=" -d grant_type=authorization_code -d code=$CODE -d redirect_uri=$URL https://accounts.spotify.com/api/token """
   
    """ Hiermee zullen we een object krijgen met de access token """

    context = {
        'code': code 
    }
    return render(request, 'template/spotify.html', {'context': context})



""" YOUTUBE """
def youtube(request):
    return HttpResponse('youtube')


""" SNAKE """
def snake(request):
    return HttpResponse('snake')


""" 
    birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'

    client_credentials_manager = SpotifyClientCredentials('ff1a2ba0fcd642fbb63b304eeaf19c90', 'da1063054cfe4af19ee2ad4d21f51dc7')
    spotify = spotipy.Spotify(client_credentials_manager)

    results = spotify.artist_albums(birdy_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])
"""
