from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from projects.views import ProjectViewSet, UserViewSet, RegisterView
from issues.views import IssueViewSet
from comments.views import CommentViewSet


router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet, basename='projects')

projects_router = routers.NestedSimpleRouter(router,
                                             r'projects',
                                             lookup='projects')
projects_router.register(r'issues',
                         IssueViewSet,
                         basename='issues')
projects_router.register(r'users',
                         UserViewSet,
                         basename='users')

issues_router = routers.NestedSimpleRouter(projects_router,
                                           r'issues',
                                           lookup='issues')
issues_router.register(r'comments',
                       CommentViewSet,
                       basename='comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',
         TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/',
         TokenRefreshView.as_view(),
         name='token_refresh'),
    path('signup/',
         RegisterView.as_view(),
         name='auth_register'),
    path(r'', include(router.urls)),
    path(r'', include(projects_router.urls)),
    path(r'', include(issues_router.urls)),
]
