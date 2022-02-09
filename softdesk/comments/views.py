from rest_framework import viewsets
from rest_framework.throttling import UserRateThrottle

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Comments
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    throttle_classes = [UserRateThrottle]
