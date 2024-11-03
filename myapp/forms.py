from django import forms


class CreateNewTask(forms.Form):
  title = forms.CharField(label="Task title", max_length=200)
  description = forms.CharField(widget=forms.Textarea, label="Description",)
  
class CreateNewProject(forms.Form):
  title = forms.CharField(label="Task title", max_length=200)
  description = forms.CharField(widget=forms.Textarea, label="Description",)