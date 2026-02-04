#stickynotes/urls.py 

from django.urls import path
from .views import(
    sticky_note_list,
    sticky_note_detail,
    sticky_note_create,
    sticky_note_edit,
    sticky_note_delete,
)

urlpatterns=[
    path('', sticky_note_list, name='sticky_note_list'),
    path('note/<int:pk>/', sticky_note_detail, name='sticky_note_detail'),
    path('note/new/', sticky_note_create, name='sticky_note_create'),
    path('note/<int:pk>/edit/', sticky_note_edit, name='sticky_note_edit'),
    path('note/<int:pk>/delete/', sticky_note_delete, name='sticky_note_delete'),   
]
