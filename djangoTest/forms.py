from django import forms
from .models import Board


class AddWork(forms.ModelForm):
    class Meta:
        model = Board
        fields = ("name", "text", "category")