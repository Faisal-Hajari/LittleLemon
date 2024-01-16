from django.urls import path 
from . import views

urlpatterns = [ 
    #example : 
    # path("books/", views.book)
    path("menu-items", views.MenuItemView.as_view()),
]