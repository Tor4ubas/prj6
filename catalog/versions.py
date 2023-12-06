from django.shortcuts import render, get_object_or_404, redirect
from catalog.forms import VersionForm
from catalog.models import Product, Version


def version_list(request, pk):
    product = get_object_or_404(Product, pk=pk)
    versions = product.version_set.all()
    return render(request, 'catalog/version_list.html', {'product': product, 'versions': versions})


def version_create(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = VersionForm(request.POST)

        if form.is_valid():
            version = form.save(commit=False)
            version.product = product
            if request.POST.get('is_active'):
                product.version_set.update(is_active=False)
                version.is_active = True
            version.save()

            return redirect('catalog:version_list', pk=pk)
    else:
        form = VersionForm()

    return render(request, 'catalog/version_create.html', {'form': form, 'product': product})


def version_active(version_id):
    version = get_object_or_404(Version, pk=version_id)
    product = version.product

    # Установка активной версии
    product.version_set.filter(is_active=True).exclude(pk=version_id).update(is_active=False)

    version.is_active = True
    version.save()

    # Сохранение изменений в объекте продукта
    product.save()

    return redirect('catalog:version_list', product_id=product.id)


def confirm_delete_version(request, version_id):
    version = get_object_or_404(Version, pk=version_id)
    if request.method == 'POST':
        version.delete()
        return redirect('catalog:version_list', version_id=version.id)
    return render(request, 'catalog/version_delete.html', {'version': version})


def version_delete(request, pk):
    version = get_object_or_404(Version, pk=pk)

    if request.method == 'POST':
        # Обработка POST-запроса для удаления версии
        version.delete()
        return redirect('catalog:version_list', pk=version.product.id)

    return render(request, 'catalog/confirm_delete_version.html', {'version': version})


def make_active(request, pk):
    version = get_object_or_404(Version, pk=pk)
    product = version.product

    # Сбрасываем активный флаг для всех версий продукта
    product.version_set.update(is_active=False)

    # Устанавливаем активный флаг для выбранной версии
    version.is_active = True
    version.save()

    return redirect('catalog:version_list', pk=product.id)
