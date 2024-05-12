from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSeriallizer


# we import the Token model that stores tokens
from rest_framework.authtoken.models import Token

from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.


@api_view(["POST",])
def logout_user(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response({"message": "You are logged out successfully."}, status=status.HTTP_200_OK)


@api_view(["POST",])
def user_register_view(request):
    if request.method == "POST":
        serializer = UserRegisterSeriallizer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()

            # creating the payload
            data["response"] = "Account has been created"
            data["username"] = account.username
            data["email"] = account.email

            # this is when we want token from Token Authentication.
            # getting the token
            # token = Token.objects.get(user=account).key

            # data["token"] = token

            # When we use jsonwebtoken.

            # we get and store the refresh token for the user who is registering.
            refresh = RefreshToken.for_user(account)

            # we create the token payload that contains the access and refresh token.
            data["token"] = {
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }
        else:
            data = serializer.errors
        return Response(data)
