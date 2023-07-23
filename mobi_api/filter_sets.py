from django_filters.rest_framework import RangeFilter, FilterSet
from .models import mobile

class range_filter(FilterSet):
    price = RangeFilter()

    class Meta:
        model = mobile
        fields = ['price']