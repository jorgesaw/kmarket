"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from apps.users.permissions import (
    IsAccountOwner, 
    IsActiveUser
)

# Serializers
from apps.users.serializers.profiles import ProfileModelSerializer
from apps.users.serializers import (
    AccountVerificationSerializer, 
    UserLoginSerializer, 
    UserModelSerializer, 
    UserSignUpSerializer
)

# Models
from apps.users.models import User


class UserViewSet(mixins.RetrieveModelMixin, 
                    mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet):
    """User view set.

    Handle sign up, login and account verification.
    """

    queryset = User.objects.filter(active=True, is_client=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        """Assign permissions based on action."""

        if self.action in ['signup', 'verify']:
            permissions = [AllowAny,]
        elif self.action == 'login':
            permissions = [IsActiveUser,]
        elif self.action in ['update', 'partial_update']:
            permissions = [IsAuthenticated, IsAccountOwner]
        elif self.action == 'retrieve':
            permissions = [IsAuthenticated,]
        else:
            permissions = [IsAuthenticated,]
        
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """ User sign up."""

        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def verify(self, request):
        """Account verification."""

        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Congratulation, tu account has verified.'}
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['put', 'patch'])
    def profile(self, request, *args, **kwargs):
        """Update profile data."""

        user = self.get_object()
        profile = user.profile
        partial = request.method == 'PATCH'
        serializer = ProfileModelSerializer(
            profile, 
            data=request.data, 
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data

        return Response(data)

    def retrieve(self, request, *args, **kwargs):
        """Add extra data to response."""

        response = super(UserViewSet, self).retrieve(request, *args, **kwargs)
        data = {
            'user': response.data, 
        }
        response.data = data

        return response

class UserLoginAPIView(APIView):
    """User Login API view."""

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)


class UserSignUpAPIView(APIView):
    """User sign up API view."""

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""

        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)


class AccountVerificationAPIView(APIView):
    """User account verification API view."""

    def post(self, request, *args, **kwargs):
        """Handle HTTP POST request."""

        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Congratulation, tu account has verified.'}
        return Response(data, status=status.HTTP_200_OK)