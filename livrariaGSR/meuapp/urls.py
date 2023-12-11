from django.urls import path
from catalogos import views


urlpatterns = [
    path('', views.index, name='index'),
    path('busca/', views.busca, name='busca'),
    path('admin/', admin.site.urls),
]
