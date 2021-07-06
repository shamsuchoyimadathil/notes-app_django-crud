from django import views
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse 
from django.views.generic import ListView
from add_notes.models import Notes

def mainPage(request):
    return render(request,"Notes/main.html")


