from django.urls import path
from . import views #faça importação do views para puxar o

urlpatterns = [
    path('', views.signup, name="signup"),  # Abre a tela de login/signup ao acessar o site
    path('signup/', views.signup, name="signup_page"),
    path('pagina_home/', views.pagina_inicial_home, name="pagina_home"), # Painel do ADM após logar
    path('mello_pictures/', views.portifolio_jmello, name="mello_pictures"), # Site público dos clientes
    path('adicionar-midia/', views.adicionar_midia_adm, name="adicionar_midia"),
    path('deletar-midia/<int:id>/', views.deletar_midia, name="deletar_midia")
]