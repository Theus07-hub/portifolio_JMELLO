from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import FotoPortifolio

# Tela de Login
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')

    elif request.method == "POST":
        user_digitado = request.POST.get('user')
        senha_digitada = request.POST.get('password')

        usuario_correto = "Jmello21"
        senha_correta = "Mac2025*@"

        if user_digitado == usuario_correto and senha_digitada == senha_correta:
            # SUCESSO! Criamos o "crachá" de autenticação na sessão do navegador
            request.session['admin_logado'] = True

            # Redireciona para o painel do ADM
            return redirect('pagina_home')
        else:
            erro_msg = "Usuário ou senha incorretos!"
            return render(request, 'signup.html', {'erro': erro_msg})


# Painel do ADM (AGORA PROTEGIDO!)
def pagina_inicial_home(request):
    # Verifica se o "crachá" existe na sessão. Se não tiver logado, expulsa para o login!
    if not request.session.get('admin_logado'):
        return redirect('signup')

    fotos = FotoPortifolio.objects.exclude(imagem='')
    videos = FotoPortifolio.objects.exclude(video='')
    contexto = {
        'fotos': fotos,
        'videos': videos,
        'eh_admin': True
    }
    return render(request, "pagina_home.html", contexto)


# Rota pública dos visitantes (Continua livre para todos)
def portifolio_jmello(request):
    fotos = FotoPortifolio.objects.exclude(imagem='')
    videos = FotoPortifolio.objects.exclude(video='')
    contexto = {
        'fotos': fotos,
        'videos': videos,
        'eh_admin': False
    }
    return render(request, "mello_pictures.html", contexto)


# Proteger também a adição de mídia
def adicionar_midia_adm(request):
    if not request.session.get('admin_logado'):
        return redirect('signup')

    if request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        imagens = request.FILES.getlist('imagem')
        videos = request.FILES.getlist('video')

        for img in imagens:
            FotoPortifolio.objects.create(titulo=titulo, descricao=descricao, imagem=img)

        for vid in videos:
            FotoPortifolio.objects.create(titulo=titulo, descricao=descricao, video=vid)

        return redirect('pagina_home')

    return redirect('pagina_home')


# Proteger também a exclusão de mídia
def deletar_midia(request, id):
    if not request.session.get('admin_logado'):
        return redirect('signup')

    midia = get_object_or_404(FotoPortifolio, id=id)
    midia.delete()
    return redirect('pagina_home')
