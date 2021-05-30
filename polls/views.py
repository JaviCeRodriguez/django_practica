from django.shortcuts import render
from django.http import HttpResponse

def index(reques):
    return HttpResponse('Hola! Estoy haciendo un index para "polls".')