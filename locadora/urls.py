from django.contrib import admin
from django.urls import path
from .views import filme_criar, filme_editar, filme_remover, filme_listar, index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('filme/',filme_criar,name='filme_criar'),
    path('filme/editar/<int:id>/',filme_editar, name='filme_editar'),
    path('filme/remover/<int:id>/',filme_remover,name='filme_remover'),
    path('filme/listar',filme_listar,name='filme_listar'),
]