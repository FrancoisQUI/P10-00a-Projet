from pprint import pprint

from rest_framework.response import Response
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

    def list(self, request, *args, **kwargs):
        pprint(kwargs)
        queryset = Issue.objects.filter(project_id=kwargs['projects_pk'])
        serializer = IssueSerializer(queryset, many=True)
        return Response(serializer.data)

