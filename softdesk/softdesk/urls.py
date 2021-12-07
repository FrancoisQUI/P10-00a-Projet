from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from projects.views import ProjectViewSet
from comments.views import CommentViewSet


router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('rest_framework.urls')),
    path(r'', include(router.urls))
]
