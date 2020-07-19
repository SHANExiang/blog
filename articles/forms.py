from django import forms
from ckeditor_uploader.fields import RichTextUploadingField



class ArticleForm(forms.Form):
    title = forms.CharField(label='标题', max_length=128, widget=forms.
                            Textarea(attrs={'class': 'form-control',
                                            'placeholder': 'Title',
                                            'autofocus': ''}))
    text = RichTextUploadingField()
