from pprint import pprint

from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.throttling import UserRateThrottle
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrContributor, IsOwner

from .models import Project, Contributor
from .serializers import ProjectSerializer, \
    RegisterSerializer, ContributorSerializer


class ProjectViewSet(ModelViewSet):
    """
    API Endpoint that allows Projects to be viewed and edited
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrContributor]
    throttle_classes = [UserRateThrottle]

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
            # TODO: Save Author as Contributor
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        queryset = Project.objects.get(pk=kwargs["pk"])
        serializer = ProjectSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        project = self.get_object()
        self.perform_destroy(project)
        return Response(data={"detail": "Project successfully destroyed"},
                        status=status.HTTP_204_NO_CONTENT)


class UserViewSet(ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    throttle_classes = [UserRateThrottle]

    def list(self, request, *args, **kwargs):
        queryset = Contributor.objects.filter(project_id=kwargs["projects_pk"])
        serializer = ContributorSerializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        print("Je détruit un Utilisateur! Hahahaha!")
        queryset = Contributor.objects.get(
            user_id_id=kwargs['pk'],
            project_id_id=kwargs['projects_pk'])
        self.perform_destroy(queryset)
        return Response(data={"detail": "User successfully removed from project"},
                        status=status.HTTP_204_NO_CONTENT)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    throttle_classes = [UserRateThrottle]
