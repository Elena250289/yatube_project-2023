from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


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
