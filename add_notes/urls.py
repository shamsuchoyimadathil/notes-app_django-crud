from django.urls import path 
from . import views

urlpatterns = [
    path("",views.AddNote.as_view() , name="add-notes"),
    path("thank-you",views.ThankYou.as_view(), name="thank-you"),
    path("all-notes",views.AllNotes.as_view(),name="all-notes"),
    path("detail-note/<int:pk>",views.SingleNotes.as_view(),name="detail-note"),
    path("delete-note/<int:pk>",views.DeleteNotes.as_view(),name="delete-note"),
    path("update-note/<int:pk>",views.UpdateNotes.as_view(),name="update-note")
]
