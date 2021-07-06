from django.db.models import fields
from .models import Notes
from django import forms


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes 
        fields = "__all__"
        labels = {
            "name":"Heading of your note",
            "note":"Notes",
            "image":"Related Image"
        } 
        error_message = {
            "name":{
                "required":"Your name must not be empty"
            }
        } 

