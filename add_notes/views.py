from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView , DetailView
from django.views.generic.edit import DeleteView , UpdateView
from django.views import View
from django.views.generic.base import TemplateView

from . models import Notes
from . forms import NotesForm
#Create your views here.

class AddNote(View):
    def get(self,request):
        form = NotesForm
        return render(request,"add_notes/add-notes.html",{
            "form":form
        })

    def post(self,request):
        form = NotesForm(request.POST , request.FILES ,)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("thank-you") 


        return render(request,"add_notes/add-notes.html",{
            "form":form
        }) 

class ThankYou(TemplateView):
    template_name = "add_notes/thank-you.html" 

class AllNotes(ListView):
    template_name = "add_notes/all-notes.html" 
    model = Notes
    ordering = ['-id']
    context_object_name = "all_notes" 

class SingleNotes(DetailView):
    template_name = "add_notes/detail-note.html"
    model = Notes   
    context_object_name = "detail" 

class DeleteNotes(DeleteView):
    template_name = "add_notes/detail-note.html" 
    model = Notes 
    success_url = "/" 

class UpdateNotes(UpdateView):
    template_name = "add_notes/add-notes.html"
    model =  Notes 
    fields = [
        "name",
        "note"
    ]
    success_url = "/" 
