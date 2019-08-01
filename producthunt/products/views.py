from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product


def home(request):
    return render(request, 'products/home.html')


@login_required()
def create(request):
    if request.method == 'POST':
        title = request.POST['product_title']
        body = request.POST['product_body']
        url = url_refined(request.POST['product_url'])
        icon = request.FILES['product_icon']
        image = request.FILES['product_image']
        hunter = request.user
        try:
            product = Product(title=title, body=body, url=url, icon=icon, image=image, hunter=hunter)
            product.save()
            messages.success(request, 'Product has been created successfully!')
            return redirect(f'/products/{str(product.id)}/details/')
        except:
            error_messages = ["Product didn't created! Please try again"]
            return render(request, 'products/create.html', {'messages': error_messages})

    else:
        return render(request, 'products/create.html')


def details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/details.html', {'product': product})


def url_refined(url_text):
    return 'https://' + url_text if 'http' not in url_text else url_text
