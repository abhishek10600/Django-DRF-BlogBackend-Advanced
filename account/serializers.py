from django.contrib.auth.models import User
from rest_framework import serializers


class UserRegisterSeriallizer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    # we override the save() method because password2 is not present by default and we also need to compare password and password2 and we also want to check if user with same email exists or not.
    def save(self):
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError(
                {"Error": "Password does not match"})
        if User.objects.filter(email=self.validated_data["email"]).exists():
            raise serializers.ValidationError(
                {"Error": "User with email already exists."})
        account = User(
            email=self.validated_data["email"], username=self.validated_data["username"])
        account.set_password(password)  # this will hash the password
        account.save()
        return account
