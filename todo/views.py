from django.shortcuts import render
from .models import Todo, Category



# Create your views here.
def home(request):
    category = Category.objects.all()
    todo =  Todo.objects.all().filter(category__in=category)
    context = {
        'todos':todo,
    }
    return render(request, 'todo/home.html', context)