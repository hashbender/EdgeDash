from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def main_page(request):
    print "Loading main page"
    return render_to_response('index.html')

def other_page(request):
    print "Loading other page"

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
