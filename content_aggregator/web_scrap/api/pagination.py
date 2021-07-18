from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination
	)

class NewsLimitOffsetPagination(LimitOffsetPagination):
	default_limit=3
	max_limit=5

class NewsPageNumberPagination(PageNumberPagination):
	page_size=3