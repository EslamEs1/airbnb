from pyexpat import model
from attr import fields
from rest_framework import serializers
from .models import About , FAQ


class About_Serializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"


class FAQ_Serializers(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"