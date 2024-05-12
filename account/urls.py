from django.urls import path, include

# this is used to create new token for the user in the database and return that token to the user. We use obtain_auth_token when we are using TokenAuthentication.
# from rest_framework.authtoken.views import obtain_auth_token


# we import this when we use this JwtAuthentication.
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from . import views


urlpatterns = [

    # Token Authentication

    # this route is used for login and obtain_auth_token will give us the token for the user when we provide the correct username and password of that user, if token does not exits meaning it is a new user then it will create a new token for the user and give us the token for that user.
    # path("register/", views.user_register_view, name="register"),
    # path("login/", obtain_auth_token, name="login"),
    # path("logout_user/", views.logout_user, name="logout_user")



    # Jsonwebtoken Authentication

    # this is to register a new user
    path("register/", views.user_register_view, name="register"),

    # this is used to login and obtain the access token and the refresh token.
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # this url is used to obtain the new access token after the old access token is expired and we need to pass the refresh token.
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path to logout the user.
    path("logout_user/", views.logout_user, name="logout_user")
]
