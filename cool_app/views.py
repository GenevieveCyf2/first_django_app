from django.shortcuts import render, HttpResponse
from cool_app.game import kalu, david

# Random python code
name = "Genevie"
friends = ['Bob', 'Sally', 'Jon']

message = ""
for friend in friends:
    message += friend + " is my good friend. "

# display your result of whateevr we want to the world.
# Create your views here.
def home(self):
    return HttpResponse(message)