from django import forms
from .models import Publisher, Newsletter, Article


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['title', 'content', 'publisher']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'publisher']
