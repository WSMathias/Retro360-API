from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Retro360User, Retro360Board, Retro360Feedback
from django.contrib.auth.models import User

class RetroUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class UserSerializer(serializers.ModelSerializer):
    boards = serializers.PrimaryKeyRelatedField(many=True, queryset=Retro360Board.objects.all())
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    is_staff = serializers.BooleanField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name','last_name','email','is_staff','boards','password')

    def create(self, validated_data):
        cleaneData ={
            'username': validated_data['username'],
            'first_name': validated_data['first_name'],
            'last_name': validated_data['last_name'],
            'email': validated_data['email'],
        }
        user = super(UserSerializer, self).create(cleaneData)
        user.is_staff=False
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class BoardSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Retro360Board
        fields = ('id','board_name','board_admin','board_members')

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retro360Feedback
        fields = ('id','feedback_from','feedback_to','board','content')