from django.urls import path,include
from .views import home_page_view
from django.contrib import admin


urlpatterns=[
      path('admin/', admin.site.urls),
       path('',HomePageView.as_view(), name='index'),
       path('catalogo',CatalogoPageView.as_view(), name='catalogo'),
   
]