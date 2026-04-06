from rest_framework import viewsets
from elements.models import Element, Category, Type
from .serializers import ElementSerializer , CategorySerializer, TypeSerializer, CommentSerializer
from coments.models import Comment



class ElementViewSet(viewsets.ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.exclude(element__isnull=True)
    serializer_class = CommentSerializer

