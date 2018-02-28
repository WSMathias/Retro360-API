from retro_app.models import Retro360Board, Retro360Feedback
from django.contrib.auth.models import User
from retro_app.serializers import UserSerializer, BoardSerializer, FeedbackSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsAdminOrReadOnly , IsAuthenticatedOrSignup
from rest_framework.views import APIView
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny

class UserList(generics.ListCreateAPIView):
    """
    List  and Create Users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrSignup,)

class UserDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retriew, Update and Delete User
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class Logout(APIView):
    """
    Logout
    """
    queryset = User.objects.all()
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class BoardFeedbackViewset(viewsets.ModelViewSet):
    """
    List Feedbacks for requested Board
    """
    queryset = Retro360Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request,board_id=None, *args, **kwargs):
        instance = self.get_queryset().filter(board__id=board_id)
        serializer = self.get_serializer(instance,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class FeedbackList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    List Feedbacks and Create Feedback
    """
    
    queryset = Retro360Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class FeedbackDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retriew, Update and Delete Feedback
    """
    queryset = Retro360Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BoardList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
        List Boards and Create Board
    """
    
    queryset = Retro360Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BoardDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
        Retriew, Update and Delete Board
    """
    queryset = Retro360Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
