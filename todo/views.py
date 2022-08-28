from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo, Category
from .forms import TodoForm, CategoryForm



# Create your views here.
def home(request):
    category = Category.objects.all()
    todo =  Todo.objects.all().filter(category__in=category)
    context = {
        'todo':todo,
    }
    return render(request, 'todo/home.html', context)

def detail(request, id):
    # todo = Todo.object_or_404(Todo,id=id)
    todo =  get_object_or_404(Category, id=id)
    context = {
        'todo':todo
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
            form = CategoryForm()
    else:
        form = CategoryForm
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



# def detail(request, id):
#     # blog = Blog.objects.get(id=id)
#     blog = get_object_or_404(Blog,id=id)
#     context = {
#         'blog':blog
#     }
#     return render (request, 'pages/detail.html', context)    


# def update(request, id):
#     blog = get_object_or_404(Blog,id=id)
#     form = BlogForm(request.POST, instance=blog)
#     if form.is_valid():
#         form.save()
#         return redirect('blog')
#     else:
#         form = BlogForm(instance=blog)
#     context = {
#         'form':form
#     }

#     return render(request, 'pages/update.html', context)


# def delete(request, id):
#     blog = get_object_or_404(Blog,id=id)
#     blog.delete()
#     return redirect('home')