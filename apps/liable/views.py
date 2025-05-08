from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .forms import LiableForm
from .models import Liable


class Index(ListView):
    model=Liable
    template_view="liable/index.html"
    context_object_name='liables'

def index(request):

    liables = Liable.objects.all()
    if (request.GET.get('search')):
        liables = Liable.objects.filter(
            name__contains=request.GET.get('search'))

    context = {
        'liables': liables
    }
    return render(request, 'liable/index.html', context)

    

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