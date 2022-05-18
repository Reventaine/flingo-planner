from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text', 'image']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'image']
        labels = {'text': 'Entry'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}