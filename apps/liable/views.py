from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView
from .forms import LiableForm
from .models import Liable


class Index(ListView):
    model=Liable
    template_view="liable/liable_list.html"
    context_object_name='liables'

class Detail(DetailView):
    model=Liable
    template_view="liable/liable_detail.html"
    context_object_name='liable'

    

def create(request):
    if (request.method == 'GET'):
        form = LiableForm()
        context = {
            'form': form,
        }
        return render(request, 'liable/create.html', context)

    if (request.method == 'POST'):
        form = LiableForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Todo bello')