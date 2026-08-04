from Books.models import *
from django.shortcuts import render
from django.core.paginator import Paginator

def Categories(request):
    return{"Categorys": Category.objects.all()}

def Authors(request):
    return{"Authors": Author.objects.all()}

def Formats(request):
    return {"Formats": Format.objects.all()}

