from django.urls import path
from .views import home, form, detail, category, delete

urlpatterns = [
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('detail/<int:id>', detail, name='detail'),
    path('category/', category, name='category'),
    path('delete/<int:id>', delete, name="delete"),
]
