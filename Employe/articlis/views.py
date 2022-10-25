from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles, Category

#переделать в классы
def index(request):
    return render(request, 'articlis/index.html')

def articlis(request):
    article = Articles.objects.all()
    categories = Category.objects.all()
    return render(request, 'articlis/artecles.html', {'article':article, 'category':categories})

def category(request,category_id):
    article = Articles.objects.filter(category_id = category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'articlis/category.html', {'article': article , 'category': categories, 'categorise':category})