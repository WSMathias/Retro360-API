from django.shortcuts import render
from django.views.generic import (
            FormView,
            TemplateView,
            ListView,
            DetailView,
            CreateView,
            UpdateView,
            DeleteView)
from .forms import UserForm, RetroUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import models
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse


from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas
from .urls import my_patterns

@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='API Docs', patterns=my_patterns, url='/api/v1/')
    return response.Response(generator.get_schema())


class IndexView(TemplateView):
    template_name = 'retro/index.html'

# class AddRetroUserView(FormView):
#     form_class = RetroUserForm
#     template_name = 'retro/create_user_form.html'
#     success_url = 'retro:index'
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = RetroUserForm
#         return context

#     def form_valid(self,form):
#         form.save()
#         return super().form_valid(form)


class AddRetroUserView(CreateView):
    model = models.RetroUser
    fields = '__all__'
    success_url = reverse_lazy('retro:list')

class RetroUserListView(ListView):
    template_name = 'retro/retrousers_list.html'
    context_object_name = 'retrousers'
    model = models.RetroUser

class RetroUserDetailView(DetailView):
    template_name = 'retro/retrouser_detail.html'
    context_object_name = 'retrouser'
    model = models.RetroUser

class RetroUserDeleteView(DeleteView):
    model = models.RetroUser
    success_url = reverse_lazy('retro:list')

class RetroUserUpdateView(UpdateView):
    model = models.RetroUser
    fields = ['first_name','last_name','email',]
    success_url = reverse_lazy('retro:list')
# CVB form for sign up
"""
class SignUpView(FormView):
    form_class = UserForm
    template_name = 'retro/signup.html'

    form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect('home')
"""
def user_login(request):
    return HttpResponse("TODO")


def user_signup(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'retro/signup_form.html',{
        'registered':registered,
        'user_form':user_form,
    })
# Create your views here.
