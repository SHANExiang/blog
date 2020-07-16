from django import forms
from ckeditor.fields import RichTextField


class ArticleForm(forms.Form):
    title = forms.CharField(label='标题', max_length=128, widget=forms.
                            Textarea(attrs={'class': 'form-control',
                                            'placeholder': 'Title',
                                            'autofocus': ''}))
    text = RichTextField()