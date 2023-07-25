from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class defaultPagination(PageNumberPagination):
    page_size = 15
    max_page_size = 50
    page_size_query_param = 'page-size'
    
    