from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializers

class MenuItemView(generics.ListAPIView): 
    queryset = MenuItem.objects.all() 
    serializer_class = MenuItemSerializers