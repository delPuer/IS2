from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from .models import UserStory
from proyecto.models import *
from userstory.forms import CreateUserStoryForm, UpdateUserStoryForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


@method_decorator(login_required, name='dispatch')
class UserStoryListView(LoginRequiredMixin, ListView):
    template_name = 'userstory/list.html'
    model = UserStory
    queryset = UserStory.objects.all()

    def get(self,request,*args,**kwargs):
        self.object = None
        self.object_list = UserStory.objects.filter(proyecto=self.kwargs['pk_proyecto'])
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        return self.render_to_response(self.get_context_data(project=proyecto,object_list=self.object_list))

@method_decorator(login_required, name='dispatch')
class CreateUserStoryView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'userstory/userstory.html'
    model = UserStory
    success_url = '../'
    form_class = CreateUserStoryForm
    success_message = 'Se ha creado el user story'

    def get_object(self, queryset=None):
        obj = UserStory()
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        obj.proyecto = proyecto
        return obj

    def get(self,request,*args,**kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Crear User Story"
        return context


@method_decorator(login_required, name='dispatch')
class UpdateUserStoryView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'userstory/userstory.html'
    model = UserStory
    form_class = UpdateUserStoryForm
    success_url = '../'
    success_message = 'Los cambios se guardaron correctamente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modificar User Story"
        return context

    def get_object(self, queryset=None):
        return UserStory.objects.get(pk=self.kwargs['pk'])

    def get_absolute_url(self):
        return reverse('update_userstory', kwargs={'pk': self.kwargs['pk']})

@method_decorator(login_required, name='dispatch')
class ProductBacklogListView(LoginRequiredMixin, ListView):
    template_name = 'userstory/ProductBacklog.html'
    model = UserStory
    queryset = UserStory.objects.all()