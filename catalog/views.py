from django.shortcuts import render
from django.urls import reverse

from catalog.models import Product


def contacts(request):
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     phone = request.POST.get('phone')
    #     message = request.POST.get('message')
    #     print(f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}')

    return render(request, 'catalog/contacts.html')


def catalog_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'catalog/catalog_list.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product,
        'product_detail_url': reverse('catalog:product_detail', kwargs={'product_id': product_id})
    }
    return render(request, 'catalog/product_detail.html', context)
