from rest_framework.pagination import LimitOffsetPagination

#Custom Pagination Class To set Limit And Offset
class CustomLimitAndOffset(LimitOffsetPagination):
    default_limit=100
    limit_query_param='limit'
    offset_query_param='offset'
    max_limit=100