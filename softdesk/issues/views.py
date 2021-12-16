from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Issue
from .serializers import IssueSerializer


class IssueViewSet(ModelViewSet):
    """
    API Endpoint that allows Projects to be viewed and edited
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]
