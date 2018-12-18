from django.shortcuts import render, get_object_or_404, render_to_response
from login_res.models import User
from .models import Category, Product
#from django.http import HttpResponseRedirect
# Create your views here.

# 根据品类显示商品
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(categories, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'sells/product/home.html',
                  {'category': category, 'categories': categories, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'detailinfo.html', {'product': product})

#发布闲置
#显示发布页面
def publish(request):
    try:
        del request.session['error']
    except:
        return render(request,'publish.html')
    return render(request)

#发布操作
def do_publish(request):
     stuid = request.session['stuid']
     users=User.objects.all()
     for i in users:
         if i.stuid==stuid:
             id=i
     name=request.POST.get('name')
     tel=request.POST.get('tel')
     description=request.POST.get('description')
     price=request.POST.get('price')
     gold=request.POST.get('gold')
     category=request.POST.get('category')
     cat=Category.objects.get(pk=category)
     img =request.FILES.get('img')
     Product.objects.create(name=name,description=description,price=price,gold=gold,category=cat,tel=tel,stuid=id,image=img)
     return render_to_response('sells/product/home.html', {'stuid': stuid})
