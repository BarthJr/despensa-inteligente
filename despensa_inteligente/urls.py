"""despensa_inteligente URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core.views import CategoriaViewSet, MedidaViewSet, ProdutoViewSet, DespensaViewSet, ProdutoDespensaViewSet, \
    ClienteViewSet, ReceitaViewSet, ProdutoReceitaViewSet, FavoritaViewSet, FazerReceitaViewSet

router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'medidas', MedidaViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'despensas', DespensaViewSet)
router.register(r'produtos_despensas', ProdutoDespensaViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'receitas', ReceitaViewSet)
router.register(r'produtos_receitas', ProdutoReceitaViewSet)
router.register(r'favoritas', FavoritaViewSet)
router.register(r'fazer_receita', FazerReceitaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
