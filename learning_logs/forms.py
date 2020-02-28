from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		labels = {'text':''}
		fields = ['text']




class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		labels = {'text': ''}
		fields = ['text']
		widgets = {'text': forms.Textarea(attrs={'cols':80})}