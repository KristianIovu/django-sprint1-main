from django.shortcuts import render


def about(request):
    """Функция отображения описания сайта."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Функция отображения правил сайта."""
    template = 'pages/rules.html'
    return render(request, template)
