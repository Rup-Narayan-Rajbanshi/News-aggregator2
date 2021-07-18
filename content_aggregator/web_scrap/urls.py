
from django.urls import path,include

from .views import *
# from apis.views import *

app_name = 'web_scrap'

urlpatterns = [
    path('news_list/', news_list, name='list'),
    path('topic_news/<int:id>/', topic_news, name='topic_news'),
    
]