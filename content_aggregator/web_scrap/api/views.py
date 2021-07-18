from rest_framework.generics import(
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .pagination import NewsLimitOffsetPagination, NewsPageNumberPagination
from web_scrap.api.serializers import *
from web_scrap.models import *

class NewsListAPIView(ListAPIView):
    queryset=Data.objects.all()
    serializer_class = NewsSerializer
    pagination_class=NewsPageNumberPagination

class NewsDetailAPIView(RetrieveAPIView):
    queryset=Data.objects.all()
    serializer_class = NewsSerializer

class NewsUpdateAPIView(UpdateAPIView):
    queryset=Data.objects.all()
    serializer_class=NewsSerializer
    

class NewsDeleteAPIView(DestroyAPIView):
    queryset=Data.objects.all()
    serializer_class=NewsSerializer