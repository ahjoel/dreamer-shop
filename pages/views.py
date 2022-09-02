from django.shortcuts import render


def home(request):
    data = {

    }
    return render(request, 'pages/home.html', data)


def shop(request):
    data = {

    }
    return render(request, 'pages/shop.html', data)


def product(request):
    data = {

    }
    return render(request, 'pages/product.html', data)
