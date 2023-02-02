from django.contrib import admin
from django.urls import path, include
from users.views import UserViewSet
from health.views import SymptomViewSet, DiagnosisViewSet, FoodViewSet
from rest_framework import routers

# Routers provide a way to automatically determine the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='customuser')
router.register(r'symptom', SymptomViewSet)
router.register(r'diagnosis', DiagnosisViewSet)
router.register(r'food', FoodViewSet)

# API URL routing. login URLs are for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]