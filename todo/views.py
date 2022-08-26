from django.shortcuts import render
from .models import Todo, Category



# Create your views here.
def home(request):
    todo =  Todo.objects.all()
    context = {
        'todos':todo,
    }
    return render(request, 'todo/home.html', context)