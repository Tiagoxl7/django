# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    context = {}
    return render(request,"index.html",context)

def product(request):
    context = {}
    return render(request,"product.html",context)

def products(request):
    context = {}
    return render(request,"product_list.html",context)

def contact(request):
    context = {}
    return render(request,"contact.html",context)
