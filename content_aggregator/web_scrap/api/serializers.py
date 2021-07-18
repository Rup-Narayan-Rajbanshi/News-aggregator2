from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField

from web_scrap.models import *

class NewsSerializer(ModelSerializer):
    # href=HyperlinkedIdentityField(
    #     view_name='web-scrap-api:news_detail',
    #     lookup_field='',
    # )
    class Meta:
        model=Data
        fields = [
            # 'href',
            'headline',
            'url',
            'text',
            'image_link'
        ]

# class NewsDetailSerializer(ModelSerializer):
#     class Meta:
#         model=Data