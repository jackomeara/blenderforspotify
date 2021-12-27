from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from base64 import b64encode
from .forms import PlaylistCrit
from .spotify import User_Request

# Create your views here.
def authorize(request):
    req = redirect('https://accounts.spotify.com/authorize?client_id=0368fc2dcae54727aac2b610be0e2d47&response_type=code&redirect_uri=http://localhost:8000/callback&scope=playlist-modify-private,playlist-modify-public')
    return req

def callback(request):
    authcode = HttpResponse(request.GET['code']).content.decode()
    user = User_Request()
    request.session['authtoken'] = user.authenticate(authcode)
    request.session['headers'] = {'Accept':'application/json',
                                  'Content-Type':'application/json',
                                  'Authorization':'Bearer '+request.session['authtoken']}
    return redirect('/home')

def home(request):
    if request.method == 'POST':
        form = PlaylistCrit(request.POST)
        if form.is_valid():
            form.save()
            #clean form data and create playlist
            fields = {'tracks':form.cleaned_data['track1'], 'artists':form.cleaned_data['artist1'], 'genres':form.cleaned_data['genre1']}
            if form.cleaned_data['choice4'] != '':
                fields[form.cleaned_data['type4']] = [fields[form.cleaned_data['type4']], form.cleaned_data['choice4']]
            if form.cleaned_data['choice5'] != '':
                if type(fields[form.cleaned_data['type5']]) != list:
                    fields[form.cleaned_data['type5']] = [fields[form.cleaned_data['type5']], form.cleaned_data['choice5']]
                else:
                    fields[form.cleaned_data['type5']].append(form.cleaned_data['choice5'])
            length = form.cleaned_data['length']
            name = form.cleaned_data['name']
            desc = 'Made By SpotiBlend'
            user=User_Request()
            recs = user.getrecommendations(fields['artists'], fields['tracks'], fields['genres'], length, request.session['headers'])
            pid = user.createplaylist(recs, desc, name, request.session['headers'])
            return redirect('/success')
        else:
            return HttpResponse('form not valid')
    else:
        form = PlaylistCrit()
        context = {"form":form}
        return render(request, 'playlistcrit.html', context)


def getplaylists(request):
    response = requests.get('https://api.spotify.com/v1/me/playlists', headers=request.session['headers'])
    playlists = response.json()['items']
    pnames = [playlist['name'] for playlist in playlists]
    return HttpResponse(pnames)

def success(request):
    return render(request, 'success.html')

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faqs.html')

def contact(request):
    return render(request, 'contact.html')

def landing(request):
    return render(request, 'landing.html')