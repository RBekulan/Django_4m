from django.shortcuts import HttpResponse, redirect, render
from datetime import datetime
from posts.models import Product, Review_comm


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def product_detail_view(request, id):
    if request.method == 'GET':
        post = Product.objects.get(id=id)
        comments = Review_comm.objects.filter(product=post)
        context = {
            'post': post,
            'comments': comments
        }
        return render(request, 'products/detail.html', context=context)


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
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