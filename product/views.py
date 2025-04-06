from django.shortcuts import render,redirect

from product.forms import ProductForm
from .models import Product
# Create your views here.
def index (request):
    product = Product.objects.all()
    return render(request,'index.html',{'product':product})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProductForm()

    return render(request,'create_product.html',{'form':form})