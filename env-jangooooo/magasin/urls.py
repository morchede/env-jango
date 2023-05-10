from django.urls import path
from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('products/', views.index, name='index'),
    path('', views.indexA, name='indexA'),
    path('fournisseurs/', views.indexF, name='fournisseurs'),
    path('Catalogue/', views.Catalogue, name='Catalogue'),
    path('nouvFournisseur/',views.nouveauFournisseur,name='nouvFournisseur'),
    path('register/',views.register, name = 'register'), 
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('produit/<int:product_id>/', views.detail_product, name='detail_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)