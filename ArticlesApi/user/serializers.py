from rest_framework import serializers
from rest_framework.authtoken.models import Token

from user.models import User



class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'password', 'username','email')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        ## Create user token
        token = Token.objects.create(user = user)
        return user