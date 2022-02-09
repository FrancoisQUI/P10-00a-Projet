from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated
from .permissions import IsProjectAuthorOrContributor

from .models import Issue
from .serializers import IssueSerializer


class IssueViewSet(ModelViewSet):
    """
    API Endpoint that allows Projects to be viewed and edited
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsProjectAuthorOrContributor]
    throttle_classes = [UserRateThrottle]

    def list(self, request, *args, **kwargs):
        queryset = Issue.objects.filter(project_id=kwargs['projects_pk'])
        serializer = IssueSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        issue = Issue(author_user_id_id=request.data["author_user_id"],
                      assignee_user_id_id=request.data["assignee_user_id"])
        serializer = IssueSerializer(issue, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        queryset = get_object_or_404(
            Issue,
            pk=kwargs['pk']
        )
        self.perform_destroy(queryset)

        return Response(data={"detail": "Issue successfully destroyed"},
                        status=status.HTTP_204_NO_CONTENT)


