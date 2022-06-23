from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
from .models import *


# Create your views here.

class EmojiViewSet(viewsets.ModelViewSet):
    serializer_class = GetEmojiSerializer
    queryset = Emoji.objects.all()
    http_method_names = ["get", "post"]
