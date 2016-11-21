from django.shortcuts import render, redirect


def home(request):

     # verifica se o usuário fez login
    if request.user.is_authenticated():
        return render(request, 'core/admin.html')

    # se o usuário não fez login o django renderiza
    # o arquivo que exibe a página de login
    return redirect('login')