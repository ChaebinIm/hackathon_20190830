from django.urls import path
from . import views

urlpatterns = [
    path('notice', views.noticeList.as_view()),
    path('home', views.homeList.as_view()),
    path('home/<str:addr>', views.homeDetail.as_view()),
    path('status', views.statusList.as_view()),

]