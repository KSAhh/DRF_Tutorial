from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# API를 자동으로 routing 함
# API 탐색위해 로그인 URL 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('snippets/', include('snippets.urls')),
]
