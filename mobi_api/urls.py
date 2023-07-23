from django.urls import path
from .views import mobileListView, mobileDetailView, mobileCreateView, mobileUpdateView, mobileDestroyView, test


urlpatterns = [
    path('mobiles/', mobileListView.as_view(), name='mobile-list'),
    path('mobiles/<str:slug>', mobileDetailView.as_view(), name='mobile-detail'),
    path('mobiles/create/', mobileCreateView.as_view(), name='create-mobile'),
    path('mobiles/update/<int:pk>', mobileUpdateView.as_view(), name='update-mobile'),
    path('mobiles/delete/<int:pk>', mobileDestroyView.as_view(), name='destroy-mobile'),
    path('test/', test)

]
