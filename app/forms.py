from django import forms

# Craete forms here
from app.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model = Webpage
        fields = '__all__'
        #fields=['topic_name','name','email']
        #exclude=['email']
        # widgets={'topic_name':forms.RadioSelect}
        labels={'topic_name':'TOPIC NAME'}
        help_texts={'name':'Name should not start with letter a or A','topic_name':'Select any one topic name from the list'}
        # help_texts used to give instructions for user while entering the data
