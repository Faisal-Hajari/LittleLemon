from django.urls import path 
from . import views

urlpatterns = [ 
    #example : 
    # path("books/", views.book)
    path("menu-items", views.menu_item_list),
    path("menu-items/<int:pk>", views.SingleMenuItemView.as_view()),
]