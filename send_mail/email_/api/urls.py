from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('employee', views.Employee_viewset, basename='employee')
# router.register('schedule_mail', views.schedule_mail, basename='schedule_mail')


urlpatterns = [
    path('api/', include(router.urls)),
]
