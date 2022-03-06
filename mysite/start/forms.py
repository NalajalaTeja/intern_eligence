from django.forms import ModelForm
from .models import UploadTopics

class TopicForm(ModelForm):
    class Meta: 
        model = UploadTopics
        fields = '__all__'