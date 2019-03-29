from django.http import HttpResponseRedirect
from django.shortcuts import render
from product.forms import ProductForm
from product.models import Product


def index(request):
    return render(request, 'product/index.html', {'products': Product.objects.all()})


def add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm()

    return render(request, 'product/form.html', {'form': form})
