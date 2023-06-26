from django.shortcuts import render

# Create your views here.


# Главная страница
def index(request):
    template = 'posts/index.html'
    title = 'Главная страница'
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': "Это главная страница проекта Yatube",
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


# Страница со списком мороженого
def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Главная страница'
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': "Здесь будет информация о группах проекта Yatube",
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)
