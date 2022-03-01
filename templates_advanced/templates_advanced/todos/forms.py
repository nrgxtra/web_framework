from django import forms

from templates_advanced.todos.models import Todo


class CreateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
