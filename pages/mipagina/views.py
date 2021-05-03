from django.views.generic.base import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

class CatalogoPageView(TemplateView):
    template_name = 'catalogo.html'

