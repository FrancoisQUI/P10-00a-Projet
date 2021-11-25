from rest_framework import viewsets

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API Endpoint that allows Projects to be viewed and edited
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
