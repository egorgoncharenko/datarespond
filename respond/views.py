from django.shortcuts import render
from .models import Respondent
from django.core.paginator import Paginator

#respondent = Respondent.objects.get(phone=None)

def respondents(request):
    search_query = request.GET.get('search')
    queryset = Respondent.objects.all()

    if search_query:
        queryset = queryset.filter(full_name__contains=search_query, okpo__contains=search_query, inn__contains=search_query, okved__contains=search_query)

    # Количество записей на странице
    items_per_page = 100

    # Создаем объект Paginator с указанием queryset и количества элементов на странице
    paginator = Paginator(queryset, items_per_page)

    # Получаем номер запрошенной страницы из GET-параметра
    page_number = request.GET.get('page')

    # Получаем объект страницы с указанным номером
    page = paginator.get_page(page_number)

    # Получаем записи, относящиеся к текущей странице
    respondents = page.object_list
    phones = page.object_list
    emails = page.object_list

    context = {
        'respondents': respondents,
        'search_query': search_query,
        'page': page,
    }

    return render(request, 'respondents.html', context)


