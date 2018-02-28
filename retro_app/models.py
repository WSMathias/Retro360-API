from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect

class Retro360User(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default='0')
    user_type = models.CharField(max_length= 5,default='user')
    
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return HttpResponseRedirect(reverse('retro:list'))

class Retro360Board(models.Model):
    board_admin = models.ForeignKey('auth.User', related_name='boards', on_delete=models.CASCADE)
    board_name = models.CharField(max_length=256)
    board_members = models.ManyToManyField(User,related_name='board_member',blank=True)
    def __str__(self):
        return self.board_name

class Retro360Feedback(models.Model):
    feedback_from = models.ForeignKey('auth.User',related_name='feedback_from',on_delete=models.CASCADE)
    feedback_to = models.ForeignKey(User,related_name='feedback_to',on_delete=models.CASCADE)
    board = models.ForeignKey(Retro360Board,related_name='feedback',on_delete=models.CASCADE)
    content = models.CharField(max_length=256)

    def __str__(self):
        return self.content