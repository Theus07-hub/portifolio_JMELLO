from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import FotoPortifolio
# Create your views here.

#Parte feita com re-edição de IA. Foi usada somente para correção.
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')

    elif request.method == "POST":
        # Pega o que o usuário digitou no formulário
        user_digitado = request.POST.get('user')
        senha_digitada = request.POST.get('password')

        # Credenciais corretas
        usuario_correto = "Jmello21"
        senha_correta = "Mac2025*@"

        # Validação no servidor (Backend)
        if user_digitado == usuario_correto and senha_digitada == senha_correta:
            # SUCESSO!
            print("========================================")
            print(f"  LOGIN COM SUCESSO! Usuário: {user_digitado}")
            print("========================================")

            # Redireciona para a página inicial do portfólio
            return redirect('pagina_home')
        else:
            # FALHA!
            print("========================================")
            print(f"   FALHA DE LOGIN!")
            print(f"   Usuário tentado: {user_digitado}")
            print(f"   Senha tentada: {senha_digitada}")
            print("========================================")

            # Recarrega a página de login enviando uma mensagem de erro
            erro_msg = "Usuário ou senha incorretos!"
            return render(request, 'signup.html', {'erro': erro_msg})

#Parte aonde entra o portifólio editavel (ADM)
def pagina_inicial_home(request):
    fotos = FotoPortifolio.objects.exclude(imagem='')
    videos = FotoPortifolio.objects.exclude(video='')
    contexto = {
        'fotos': fotos,
        'videos': videos,
        'eh_admin': True
    }
    return render(request, "pagina_home.html", contexto)


#Rota para visualização somente de usuários.
def portifolio_jmello(request):
    fotos = FotoPortifolio.objects.exclude(imagem='')
    videos = FotoPortifolio.objects.exclude(video='')
    contexto = {
        'fotos': fotos,
        'videos': videos,
        'eh_admin': False
    }
    return render(request, "mello_pictures.html", contexto)


def adicionar_midia_adm(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        imagens = request.FILES.getlist('imagem')
        videos = request.FILES.getlist('video')

        # Salva cada imagem enviada separadamente no banco
        for img in imagens:
            FotoPortifolio.objects.create(
                titulo=titulo,
                descricao=descricao,
                imagem=img
            )

        # Salva cada vídeo enviado separadamente no banco
        for vid in videos:
            FotoPortifolio.objects.create(
                titulo=titulo,
                descricao=descricao,
                video=vid
            )

        return redirect('pagina_home')

    return redirect('pagina_home')


def deletar_midia(request, id):
    midia = get_object_or_404(FotoPortifolio, id=id)
    midia.delete()
    return redirect('pagina_home')