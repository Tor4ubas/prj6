from django.shortcuts import render
from catalog.models import Product
def contacts(request):
    #if request.method == 'POST':
        #name = request.POST.get('name')
        #phone = request.POST.get('phone')
        #message = request.POST.get('message')
        #print(f'Имя: {name}\nТелефон: {phone}\nСообщение: {message}')

    return render(request, 'catalog/contacts.html')


def catalog_list(request):
    object_list = [
  {
    "name": "Ноутбук Lenovo ThinkPad",
    "description": "Мощный ноутбук серии ThinkPad от Lenovo.",
    "photo": "product/lenovo_thinkpad.jpg",
    "category": "Ноутбуки",
    "price": 1500,
    "date_created": "2022-01-01",
    "date_updated": "2022-01-10"
  },
  {
    "name": "Смартфон iPhone 12",
    "description": "Популярный смартфон от Apple с передовыми технологиями.",
    "photo": "product/iphone_12.jpg",
    "category": "Смартфоны",
    "price": 1000,
    "date_created": "2022-02-01",
    "date_updated": "2022-02-15"
  },
  {
    "name": "Телевизор Samsung QLED",
    "description": "Высококачественный телевизор с технологией QLED от Samsung.",
    "photo": "product/samsung_qled.jpg",
    "category": "Телевизоры",
    "price": 2000,
    "date_created": "2022-03-01",
    "date_updated": "2022-03-20"
  },
  {
    "name": "Кофемашина DeLonghi Magnifica",
    "description": "Автоматическая кофемашина для приготовления вкусного кофе.",
    "photo": "product/delonghi_magnifica.jpg",
    "category": "Кофемашины",
    "price": 500,
    "date_created": "2022-04-01",
    "date_updated": "2022-04-10"
  },
  {
    "name": "Фитнес-трекер Fitbit Charge 4",
    "description": "Умный фитнес-трекер для отслеживания активности и здоровья.",
    "photo": "product/fitbit_charge_4.jpg",
    "category": "Фитнес-трекеры",
    "price": 150,
    "date_created": "2022-05-01",
    "date_updated": "2022-05-05"
  }
]

    return render(request, 'catalog/catalog_list.html', {'object_list': object_list})


def product_detail(request, product_id):
  product = Product.objects.get(id=product_id)
  return render(request, 'product_detail.html', {'product': product})
