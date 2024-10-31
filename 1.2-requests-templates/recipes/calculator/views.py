from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    return HttpResponse('готов к работе')

def recipe_view(request):
    DATA = {
        'omlet': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },
        'pasta': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        },
        'buter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        },
    }
    recipe_name = request.META['PATH_INFO'].strip('/')
    if recipe_name not in DATA.keys():
        return HttpResponse('такого рецепта нет')
    servings = int(request.GET.get('servings', 1))
    for recepie in DATA.keys():
        for key, value in DATA[recepie].items():
            DATA[recepie][key] *= servings

    context = {'recipe': DATA.get(recipe_name), 'recipe_name': recipe_name}
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
