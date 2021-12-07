from pprint import pprint

from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User
from .models import Project, Contributor


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username"
        ]


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
    contributors = ContributorSerializer(many=True)
    author_user_id = UserSerializer()

    class Meta:
        model = Project
        fields = ["title",
                  "description",
                  "type",
                  "author_user_id",
                  "contributors"]
