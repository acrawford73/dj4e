from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render #, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cat, Breed


class CatList(LoginRequiredMixin, ListView):
    def get(self, request):
        bc = Breed.objects.count()
        cl = Cat.objects.all()
        ctx = {'breed_count': bc, 'cat_list': cl}
        return render(request, 'cats/cat_list.html', ctx)

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat-all')
    template_name = 'cats/cat_form.html'

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:cat-all')
    template_name = 'cats/cat_form.html'

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = reverse_lazy('cats:cat-all')
    template_name = 'cats/cat_confirm_delete.html'


class BreedList(LoginRequiredMixin, View):
    def get(self, request):
        bd = Breed.objects.all()
        ctx = {'breed_list': bd}
        return render(request, 'cats/breed_list.html', ctx)

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed-list')
    template_name = 'cats/breed_form.html'

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:breed-list')
    template_name = 'cats/breed_form.html'

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    success_url = reverse_lazy('cats:breed-list')
    template_name = 'cats/breed_confirm_delete.html'
