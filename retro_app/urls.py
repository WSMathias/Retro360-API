from django.urls import path, include
import rest_framework_swagger
from django.contrib import admin
from . import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('user/<int:pk>',views.UserDetail.as_view(),name='userDetail'),
    path('user/',views.UserList.as_view(),name='user'),
    path('user/login/',obtain_jwt_token),
    path('user/logout/',views.Logout.as_view(),name='logout'),
    path('board/',views.BoardList.as_view()),
    path('board/<int:pk>/',views.BoardDetail.as_view()),
    path('feedback/',views.FeedbackList.as_view()),    
    path('feedback/<int:pk>/',views.FeedbackDetail.as_view()),
    path('admin/', admin.site.urls),
    path('board/<board_id>/feedbacks/',views.BoardFeedbackViewset.as_view({'get':'list'})),
]
