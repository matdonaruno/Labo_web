from django.shortcuts import render
from .models import POST
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import (ListView, DetailView, CreateView, DeleteView, UpdateView)
from . import models
from .forms import jikangaiForm

def toppage(request):
  return render(request, 'topindex.html')

def logintop(request):
  return render(request, 'logintop.html')

class jikangaiList(ListView):
  model = models.POST
  context_object_name = 'jikangaiLists'
  template_name = 'jikangaiList.html'

class jikangaiDetail(DetailView):
  model = models.POST
  context_object_name = 'jikangaiDetail'
  template_name = 'jikangaiDetail.html'

class jikangaiCreate(CreateView):
  template_name = 'jikangaiCreate2.html'
  form_class = jikangaiForm
  success_url = "{% url 'laborec:jikangaiList' %}"

class jikangaiUpdate(UpdateView):
  model = models.POST
  fields = ("create_at", "seika_fridge1", "seika_fridge2", "seika_fridge3", "seika_fridge4", "seika_fridge5", "seika_fridge6", "seika_fridge7", "seika_freezer1", "seika_samplecheck", "recorder")
  template_name = 'jikangaiUpdates.html'
  def get_success_url(self):
    return reverse('laborec:jikangaiDetail', kwargs={'pk': self.object.pk})

class jikangaiDelete(DeleteView):
  model = models.POST
  template_name = 'jikangaiDelete.html'
  success_url = reverse_lazy('laborec:jikangaiList')


def saikin(request):
  posts = POST.objects.all()
  return render(request, 'saikin.html', {'posts':posts})

def yuketuList(request):
  posts = POST.objects.all()
  return render(request, 'yuketuList.html', {'posts':posts})

def seikagaku(request):
  posts = POST.objects.all()
  return render(request, 'seikagaku.html', {'posts':posts})

def ketueki(request):
  posts = POST.objects.all()
  return render(request, 'ketueki.html', {'posts':posts})

def byouri(request):
  posts = POST.objects.all()
  return render(request, 'byouri.html', {'posts':posts})

def siyakukanri(request):
  posts = POST.objects.all()
  return render(request, 'siyakukanri.html', {'posts':posts})

