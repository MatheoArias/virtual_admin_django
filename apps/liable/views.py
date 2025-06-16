from django.views.generic import TemplateView,CreateView

class LiableIndexView(TemplateView):
    template_name='liable/liable-index.html'

class LiableCreateView(CreateView):
    template_name='liable/liable-create.html'
