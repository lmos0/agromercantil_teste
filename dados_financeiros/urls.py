from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("fetching_data", views.fetching_data, name="fetching_data"),
    path("showing_data", views.showing_data, name="showing_data"),
    path('delete_data', views.delete_data, name='delete_data'),
    path('edit_notes/<int:data_id>', views.edit_notes, name='edit_notes'),
    path("delete_note/<int:data_id>", views.delete_note, name="delete_note")
]