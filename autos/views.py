from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
#from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#from .forms import MakeForm
from .models import Autos, Make

# Create your views here.

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Make.objects.count()
        al = Autos.objects.all()
        ctx = {'make_count': mc, 'auto_list': al}
        return render(request, 'autos/autos_list.html', ctx)

### Autos
class AutosListView(LoginRequiredMixin, ListView):
    model = Autos
    context_object_name = 'auto'
    template_name = 'autos/autos_list.html'

class AutosCreateView(LoginRequiredMixin, CreateView):
    model = Autos
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
    template_name = 'autos/autos_form.html'

class AutosUpdateView(LoginRequiredMixin, UpdateView):
    model = Autos
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
    template_name = 'autos/autos_form.html'

class AutosDeleteView(LoginRequiredMixin, DeleteView):
    model = Autos
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
    template_name = 'autos/autos_confirm_delete.html'


### Make
class MakeListView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Make.objects.all()
        ctx = {'make_list': ml}
        return render(request, 'autos/make_list.html', ctx)

# class MakeListView(LoginRequiredMixin, ListView):
#     model = Make
#     context_object_name = 'make'
#     template_name = 'autos/make_list.html'

class MakeCreateView(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:make-list')
    template_name = 'autos/make_form.html'

class MakeUpdateView(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:make-list')
    template_name = 'autos/make_form.html'

class MakeDeleteView(LoginRequiredMixin, DeleteView):
    model = Make
    success_url = reverse_lazy('autos:make-list')
    template_name = 'autos/make_confirm_delete.html'
