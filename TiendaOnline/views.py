from store.models import Product
from django.shortcuts import render
from store.models import Product

def inicio(request):

    products = Product.objects.all().filter(is_available=True)
    
    context = {
        'products' : products,
    }
    return render(request,'inicio.html',context)


