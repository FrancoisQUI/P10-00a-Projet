from pprint import pprint

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

from .models import Project, Contributor


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = [
            "user_id",
            "project_id",
            "role",
            "permission",
        ]


class ProjectSerializer(ModelSerializer):
    contributors = ContributorSerializer(many=True, read_only=True)
    author_user_id = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ["title",
                  "id",
                  "description",
                  "type",
                  "author_user_id",
                  "contributors"]


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
