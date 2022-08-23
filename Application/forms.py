from django import forms
from .models import Tickets, Comments


class TicketsForm(forms.ModelForm):
    class Meta:
        model = Tickets
        exclude = []


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = []
