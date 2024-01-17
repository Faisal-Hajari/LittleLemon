from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


def search_queryset(request, queryset):
    search = request.query_params.get('search')
    if search: 
        queryset = queryset.filter(title__icontains=search)
    return queryset


def filter_queryset(request, queryset):
    title = request.query_params.get('title', None)
    price = request.query_params.get('price', None)
    inventory = request.query_params.get('inventory', None)
    category = request.query_params.get('category', None)
    category_id = request.query_params.get('category_id', None)

    if title:
        queryset = queryset.filter(title=title)
    if price:
        queryset = queryset.filter(price__lte=price)
    if inventory:
        queryset = queryset.filter(inventory=inventory)
    if category:
        queryset = queryset.filter(category__title=category)
    if category_id:
        queryset = queryset.filter(category_id=category_id)
    return queryset


def ordering(request, queryset): 
    ordering = request.query_params.get('ordering', 'title')
    queryset = queryset.order_by(ordering)
    return queryset


def menu_items_get(request): 
    queryset = MenuItem.objects.select_related('category').all()
    queryset = filter_queryset(request, queryset)
    queryset = ordering(request, queryset)
    queryset = search_queryset(request, queryset)
    serializer = MenuItemSerializers(queryset, many=True)
    return Response(serializer.data)


def menu_items_post(request): 
    serializer = MenuItemSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def menu_item_list(request):
    if request.method == 'GET': return menu_items_get(request)
    if request.method == 'POST': return menu_items_post(request)

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