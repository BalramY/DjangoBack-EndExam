from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserAccountSerializer, self).create(validated_data)



class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ("username", "password",)

