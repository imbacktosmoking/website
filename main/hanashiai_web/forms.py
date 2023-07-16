from django import forms
from .models import Post, Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('title', 'author', 'date', 'body' )

        widgets = {

            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'author':forms.Select(attrs={'class': 'form-control'}),
            'date':forms.TextInput(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'}),
        }



class Comments(forms.ModelForm):
    class Meta:
        model = Comments 
        fields = ('post','author', 'date', 'body' )

        widgets = {

            'author':forms.TextInput(attrs={'class': 'form-control'}),
            'date':forms.TextInput(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'}),
            'post':forms.Select(attrs={'class': 'form-control'}),
        }

