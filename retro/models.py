from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect

# class RetroUser(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,default='0')
#     user_type = models.CharField(max_length= 5,default='user')

#     def __str__(self):
#         return "{} {}".format(self.user.username)
    
#     def get_absolute_url(self):
#         return HttpResponseRedirect(reverse('retro:list'))
