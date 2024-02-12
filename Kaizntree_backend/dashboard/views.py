from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import CategorySerializer, TagSerializer, ItemsSerializer
from .models import Category, Tag, Items
from datetime import datetime


# Endpoint to display items dashboard
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def dashboard(request):
    items = Items.objects.all()
    serializer = ItemsSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Endpoint to add an item to dashboard
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def addItem(request):
    data = request.data
    serializer = ItemsSerializer(data=data)
    if serializer. is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)



# Endpoints to add and get category
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def category(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer. is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# Endpoint to add and get tags
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def tag(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        serializer = TagSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Endpoint to filter by item name
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def filterByName(request):
    items = Items.objects.filter(item_name=request.query_params.get('name'))
    serializer = ItemsSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Endpoint to filter by product availability status
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def filterByStatus(request):
    items = None
    if request.query_params.get('status') == '1':
        items = Items.objects.filter(available_stock__gt=100)
    else:
        items = Items.objects.filter(available_stock__lte=100)
    serializer = ItemsSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# Endpoint to filter by item added date
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def filterByDate(request):
    date_format = '%Y-%m-%d'
    start_str = request.query_params.get('start')
    start = datetime.strptime(start_str, date_format)
    end_str = request.query_params.get('end')
    end = datetime.strptime(end_str, date_format)
    items = Items.objects.filter(added_date__gte=start, added_date__lte=end)
    serializer = ItemsSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
