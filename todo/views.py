from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo, Category
from .forms import TodoForm, CategoryForm
from django.contrib import messages



# Create your views here.
def home(request):
    category = Category.objects.all()
    todo =  Todo.objects.all().filter(category__in=category)
    context = {
        'todo':todo,
    }
    return render(request, 'todo/home.html', context)

def detail(request, id):
    todo =  Todo.objects.all().filter(category=get_object_or_404(Category, id=id))
    category=get_object_or_404(Category, id=id)
    context = {
        'todo':todo,
        'category':category
    }
    return render(request, 'todo/detail.html', context)
    

def delete(request, id):
    delete = get_object_or_404(Category, id=id)
    delete.delete()
    return redirect('home')

def category(request):
    form = CategoryForm(request.POST)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form')
        else:
            messages.error(request, "Category already exists or create task")
            return redirect('category')
    else:
        form = CategoryForm()
    context = {
        'form':form
    }
    return render(request, 'todo/category.html', context)

def form(request):
    form = TodoForm(request.POST)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = TodoForm()
    else:
        form = TodoForm
    context = {
        'form':form
    }
    return render(request, 'todo/form.html', context)