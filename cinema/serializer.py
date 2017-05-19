# coding: utf-8

from rest_framework import serializers
from .models import Filme

class FilmeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filme
        depth = 1
        fields = ['id', 'title', 'synopsis', 'status']