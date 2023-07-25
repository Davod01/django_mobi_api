from .models import mobile
from .serializers import mobileSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import filters
from .pagination import defaultPagination
from .filter_sets import range_filter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class mobileListView(generics.ListAPIView):
    queryset = mobile.objects.all()
    serializer_class = mobileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,      DjangoFilterBackend]
    filterset_class  = range_filter # filters class for filtering fields like price
    search_fields = ['name', 'title', 'os']
    ordering_fields = ['price']
    pagination_class = defaultPagination


class mobileDetailView(generics.RetrieveAPIView):
    queryset = mobile.objects.all()
    serializer_class = mobileSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]

class mobileCreateView(generics.CreateAPIView):
    queryset = mobile.objects.all()
    serializer_class = mobileSerializer
    permission_classes = [IsAuthenticated]

class mobileUpdateView(generics.UpdateAPIView):
    queryset = mobile.objects.all()
    serializer_class = mobileSerializer
    permission_classes = [IsAuthenticated]

class mobileDestroyView(generics.DestroyAPIView):
    queryset = mobile.objects.all()
    serializer_class = mobileSerializer
    permission_classes = [IsAuthenticated]



@api_view(["GET"])
def get_user(requst):
    user = requst.user
    if requst.auth:
        userData = {
            'username': user.__dict__['username'],
            'first_name': user.__dict__['first_name'],
            'last_name': user.__dict__['last_name'],
            'email': user.__dict__['email'],
            'is_active': user.__dict__['is_active'],
        }
        return Response(userData)
    
    return Response({'message': 'user not authenticated' }, 401)


@api_view(["GET"])
def test(request):
    print(request.user)
    return Response('ok')