"""
URL configuration for almacen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from inicio import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='almacen/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    #path('admin/', admin.site.urls),
    path("", views.principal, name="principal"),
    path('altaArticulos', views.altaArticulos, name='altaArticulos'),
    path('alta/', views.alta, name='alta'),
    path('almacen', views.almacen, name='almacen'),
    path('reporte/pdf/', views.generar_pdf, name='generar_pdf'),
    path('eliminar/<int:articulo_id>/', views.eliminar, name='eliminar'),
    path('editar/<int:articulo_id>/', views.editar, name='editar'),
    path('reporte/pdf/', views.generar_pdf, name='generar_pdf'),
    

]
