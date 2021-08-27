# from django.contrib import admin
# from django.urls import path, include
# from rest_framework import routers
# from . import views
#
# app_name = 'plantsapp'
#
# router = routers.DefaultRouter()
# router.register('categories', views.CategoryViewSet)
# router.register('rooms', views.RoomViewSet)
# router.register('plants', views.PlantViewSet)
#
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('admin/', admin.site.urls),
#     ]