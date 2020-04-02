"""Users URLs."""
 
# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import users as users_views

"""
from apps.users.views import ( 
    UserLoginAPIView, 
    UserSignUpAPIView, 
    AccountVerificationAPIView
)
"""

router = DefaultRouter()
router.register('users', users_views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),

    #path('users/login/', UserLoginAPIView.as_view(), name='login'), 
    #path('users/signup/', UserSignUpAPIView.as_view(), name='signup'), 
    #path('users/verify/',AccountVerificationAPIView.as_view(),name='verify')
    
]