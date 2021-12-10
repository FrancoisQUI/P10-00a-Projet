from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    """
    API Endpoint that allows Projects to be viewed and edited
    """
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = Project.objects.filter(author_user_id=request.user.id)
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = Project.objects.get(pk=kwargs["pk"])
        serializer = ProjectSerializer(queryset, many=False)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        project = Project(author_user_id=self.request.user)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
