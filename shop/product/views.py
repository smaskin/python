from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from product.forms import ProductForm
from product.models import Product


def index(request):
    return render(request, 'product/index.html', {'products': Product.objects.all()})


def add(request):
    data = dict()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            products = Product.objects.all()
            data['products_html'] = render_to_string('product/list.html', {'products': products})
        else:
            data['form_html'] = render_to_string('product/form.html', {'form': form}, request=request)

    else:
        data['form_is_valid'] = False
        data['form_html'] = render_to_string('product/form.html', {'form': ProductForm()}, request=request)

    return JsonResponse(data)
