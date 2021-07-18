
from django.urls import path
from .views import *

app_name = 'web-scrap-api'

urlpatterns = [
    path('news_list/', NewsListAPIView.as_view(), name='news_list'),
    path('news_detail/<int:pk>/', NewsDetailAPIView.as_view(), name='news_detail'),
    path('news_update/<int:pk>/', NewsUpdateAPIView.as_view(), name='news_update'),
    path('news_delete/<int:pk>/', NewsDeleteAPIView.as_view(), name='news_delete'),
    ] 