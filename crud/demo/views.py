from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from demo.models import Comment
from demo.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer





# Create your views here.
