from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializers

class MenuItemView(generics.ListCreateAPIView): 
    queryset = MenuItem.objects.select_related('category').all() 
    serializer_class = MenuItemSerializers

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView): 
    queryset = MenuItem.objects.select_related('category').all() 
    serializer_class = MenuItemSerializers


"""
@api_view(['GET', 'POST'])
def menu_items(request): 
    if request.method == 'GET': 
        do stuff
    elif request.method == 'POST':
        serialized_item = MenuItemSerilizer(data=request.data)
        serialized_item.is_valid(raise_exception=True)

        #for saving use: 
        serialized_item.save()

        #to access validated data: 
        serialized_item.validated_data 

        #accessing serialized_item.data can't be done if you didn't call .save()
"""