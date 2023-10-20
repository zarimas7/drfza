
from django.urls import path
from .views import CarView, ApiCarDetail, UserRegistrationView

urlpatterns = [
    path('', CarView.as_view(), name='car'),
    path('car/<int:pk>/', ApiCarDetail.as_view(), name='car_id'),
    path('reg/', UserRegistrationView.as_view(), name='reg')
]