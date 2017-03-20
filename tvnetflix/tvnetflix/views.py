from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect

def loadIndex(request):
    return render(request, 'index.html')

def loadComedy(request):
    srcLink = "https://www.youtube.com/embed/sp79Q8Scyi8"
    return render_to_response('comedy.html', {'srcLink':srcLink})

def loadSports(request):
    srcLink = "https://www.youtube.com/embed/OlzFR-KE7iA"
    return render_to_response('sports.html', {'srcLink':srcLink})

def loadMusicVideos(request):
    srcLink = "https://www.youtube.com/embed/videoseries?list=PLUJnnrQ11_kAP-8Qm4c6mUb4LGuByQ3D4"
    return render_to_response('musicvideos.html', {'srcLink':srcLink})

def loginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('/home/')

        return render(request, "login.html")
    return render(request, "login.html")
