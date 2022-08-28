from django import forms
from .models import Todo, Category


class TodoForm(forms.ModelForm):
    todo = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'todo-input'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(
        attrs={'class': 'todo-category'}))

    class Meta():
        model = Todo
        fields = ('todo', 'category')


class CategoryForm(forms.ModelForm):
    category = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'category-input'}))

    class Meta():
        model = Category
        fields = ('category',)
