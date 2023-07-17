from django import forms
from .models import Post, Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ('image', 'title', 'author', 'date', 'body' )

        widgets = {

            'title':forms.TextInput(attrs={'class': 'form-control'}),
            'author':forms.TextInput(attrs={'class': 'form-control', 'calue':'', 'id':'author', 'type':'hidden'}),
            #'author':forms.Select(attrs={'class': 'form-control'}),
            'date':forms.TextInput(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'}),
        }



class Comments(forms.ModelForm):
    class Meta:
        model = Comments 
        fields = ( 'author','date', 'body' )

        widgets = {

            'date':forms.TextInput(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'}),
            'author':forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'comments', 'type':'hidden'}),
            

        }

