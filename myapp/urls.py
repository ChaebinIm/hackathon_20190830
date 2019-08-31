from django.urls import path
from . import views

urlpatterns = [
    path('notice', views.noticeList.as_view()),
    path('home', views.homeList.as_view()),
    path('home/<str:addr>', views.homeDetail.as_view()),
    path('status', views.statusList.as_view()),
    path('homeinfo_by_id', views.homeinfo_by_id),
    path('update_sensor_time', views.update_sensor_time),
    path('sensorData', views.sensorData),
]