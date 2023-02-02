from django.shortcuts import HttpResponse, redirect, render
from datetime import datetime
from products.models import Product, Review_comm, Category
from products.forms import ProductCreateForm, ReviewCreateForm

PAGINATION_LIMIT = 3


def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'categories/index.html', context=context)


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def detail_view(request, **kwargs):
    if request.method == 'GET':
        product = Product.objects.get(id=kwargs['id'])
        reviews = Review_comm.objects.filter(product=product)

        data = {
            'products': product,
            'comments': reviews,
            'form': ReviewCreateForm,
        }

        return render(request, 'products/detail.html', context=data)
    if request.method == 'POST':
        form = ReviewCreateForm(data=request.POST)
        if form.is_valid():
            Review_comm.objects.create(
                review=form.cleaned_data.get('review'),
                product_id=kwargs['id']
            )
            return redirect(f"/products/{kwargs['id']}/")


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        category_id = request.GET.get("category_id", None)
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if category_id:
            products = products.filter(category__in=[category_id])

        if search:
            products = products.filter(title__icontains=search)


        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        """ slice posts """
        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]
        print(products)

        context = {
            'products': products,
            'user': request.user,
            'max_page': range(1, max_page + 1),
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


def create_products(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST)

        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data['price'] if form.cleaned_data['price'] is not None else 0

            )
            return redirect('/products')

        return render(request, 'products/create.html', context={
            'form': form
        })
