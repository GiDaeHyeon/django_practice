from django.forms import ModelForm
from .models import Comment


class CommeentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']