from django.shortcuts import HttpResponse, redirect, render
from datetime import datetime
from posts.models import Product


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        posts = Product.objects.all()

        context = {
            'posts': posts
        }

        return render(request, 'products/products.html', context=context)


def greeting(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def date_(request):
    if request.method == 'GET':
        return HttpResponse(f'data{datetime.now().date()}')


def farewell(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')
