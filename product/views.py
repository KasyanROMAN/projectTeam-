from django.shortcuts import render,redirect
from django.http import HttpResponse
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



def detail(request,id_product):
    product=Product.objects.get(id=id_product)
    return render(request,'detail.html',{'product':product})
    
def delete(request,id_product):
    try:
        product=Product.objects.get(id=id_product)
        product.delete()
        return redirect('/')
    except Product.DoesNotExist:
        return HttpResponse('erorre')
    

def update(request,id_product):
    product=Product.objects.get(id=id_product)
    form=ProductForm(request.POST,instance=product)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form})