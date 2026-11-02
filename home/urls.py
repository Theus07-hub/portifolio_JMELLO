from django.urls import path
from . import views #faça importação do views para puxar o

urlpatterns = [
    path('', views.portifolio_jmello, name="home_root"),
    path('signup/', views.signup, name="signup"),
    path('pagina_home/', views.pagina_inicial_home, name="pagina_home"),
    path('mello_pictures/', views.portifolio_jmello, name="mello_pictures"),
    path('adicionar-midia/', views.adicionar_midia_adm, name="adicionar_midia"),
    path('deletar-midia/<int:id>/', views.deletar_midia, name="deletar_midia")
]