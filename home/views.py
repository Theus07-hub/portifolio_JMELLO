from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
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
            request.session['admin_logado'] = True
            return redirect('pagina_home')
        else:
            erro_msg = "Usuário ou senha incorretos!"
            return render(request, 'signup.html', {'erro': erro_msg})

# Painel do ADM
def pagina_inicial_home(request):
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

# Rota pública dos visitantes
def portifolio_jmello(request):
    fotos = FotoPortifolio.objects.exclude(imagem='')
    videos = FotoPortifolio.objects.exclude(video='')
    contexto = {
        'fotos': fotos,
        'videos': videos,
        'eh_admin': False
    }
    return render(request, "mello_pictures.html", contexto)

# Adicionar mídia via URLs vindas do Cloudinary (Upload Direto)
def adicionar_midia_adm(request):
    if not request.session.get('admin_logado'):
        return redirect('signup')

    if request.method == "POST":
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        imagem_url = request.POST.get('imagem_url')
        video_url = request.POST.get('video_url')

        # Se houver URL de foto enviada pelo widget, salva no banco
        if imagem_url:
            FotoPortifolio.objects.create(titulo=titulo, descricao=descricao, imagem=imagem_url)

        # Se houver URL de vídeo enviada pelo widget, salva no banco
        if video_url:
            FotoPortifolio.objects.create(titulo=titulo, descricao=descricao, video=video_url)

        return redirect('pagina_home')

    return redirect('pagina_home')

# Deletar mídia
def deletar_midia(request, id):
    if not request.session.get('admin_logado'):
        return redirect('signup')

    midia = get_object_or_404(FotoPortifolio, id=id)
    midia.delete()
    return redirect('pagina_home')