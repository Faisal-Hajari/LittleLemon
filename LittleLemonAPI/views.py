from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializers

class MenuItemView(generics.ListCreateAPIView): 
    queryset = MenuItem.objects.select_related('category').all() 
    serializer_class = MenuItemSerializers

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView): 
    queryset = MenuItem.objects.select_related('category').all() 
    serializer_class = MenuItemSerializers