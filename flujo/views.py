from django.views.generic import ListView, CreateView, UpdateView
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from proyecto.models import *


@method_decorator(login_required, name='dispatch')
class FlujoListView(LoginRequiredMixin, ListView):
    template_name = 'flujo/list.html'
    model = Flujo
    queryset = Flujo.objects.all()

    def get(self,request,*args,**kwargs):
        self.object = None
        self.object_list = Flujo.objects.filter(proyecto=self.kwargs['pk_proyecto'])
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        return self.render_to_response(self.get_context_data(project=proyecto,object_list=self.object_list))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Flujos de Proyecto"
        return context


@method_decorator(login_required, name='dispatch')
class UpdateFlujoView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'flujo/flujo.html'
    model = Flujo
    success_url = '../'
    form_class = CreateFlujoForm
    success_message = 'Se ha modificado el flujo'

    def get(self,request,*args,**kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        fases = Fase.objects.filter(flujo=self.object).order_by('pk')
        fases_data = []
        for fase in fases:
            d = {'nombre': fase.nombre,}
            fases_data.append(d)
        FaseFormSet = inlineformset_factory(Flujo, Fase, form=FaseForm,extra=len(fases_data))
        fases_orden_formset = FaseFormSet(initial=fases_data)
        return self.render_to_response(self.get_context_data(form=form, fases=fases_orden_formset))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modificar Flujo"
        return context

    def get_object(self, queryset=None):
        return Flujo.objects.get(pk=self.kwargs['pk'])

    def get_absolute_url(self):
        return reverse('update_project', kwargs={'pk_proyecto': self.kwargs['pk_proyecto']})

    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        fases_formset = FaseFormSet(request.POST)
        if form.is_valid() and fases_formset.is_valid():
            return self.form_valid(form,fases_formset)
        else:
            return self.form_invalid(form,fases_formset)

    def form_valid(self, form, fases_formset):
        self.object = form.save()
        fases_formset.instance = self.object
        Fase.objects.filter(flujo=self.object).delete()
        fases_formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form,fases_formset):
        return self.render_to_response(self.get_context_data(form=form, fases=fases_formset))


@method_decorator(login_required, name='dispatch')
class CreateFlujoView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'flujo/flujo.html'
    model = Flujo
    success_url = '../'
    form_class = CreateFlujoForm
    success_message = 'Se ha creado el flujo'

    def get_object(self, queryset=None):
        obj = Flujo()
        proyecto = Proyecto.objects.get(pk=self.kwargs['pk_proyecto'])
        obj.proyecto = proyecto
        return obj

    def get(self,request,*args,**kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        fases_orden_formset = FaseFormSet()
        return self.render_to_response(self.get_context_data(form=form, fases=fases_orden_formset))

    def get_context_data(self, **kwargs):
        context = super(CreateFlujoView,self).get_context_data(**kwargs)
        context['title'] = "Crear Flujo"
        return context

    def post(self,request,*args,**kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        fases_formset = FaseFormSet(request.POST)
        if form.is_valid() and fases_formset.is_valid():
            return self.form_valid(form,fases_formset)
        else:
            return self.form_invalid(form,fases_formset)

    def form_valid(self, form, fases_formset):
        self.object = form.save()
        fases_formset.instance = self.object
        fases_formset.save()
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form,fases_formset):
        return self.render_to_respose(self.get_context_data(form=form,fases=fases_formset))