from rest_framework import serializers
from .models import *


class GetEmojiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emoji
        fields = ["id", "emoji", "name", "meaning"]
