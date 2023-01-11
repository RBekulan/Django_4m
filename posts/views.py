from django.shortcuts import HttpResponse, redirect
from datetime import datetime


def greeting(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def date_(request):
    if request.method == 'GET':
        return HttpResponse(f'data{datetime.now().date()}')


def farewell(request):
    if request.method == 'GET':
        return HttpResponse('Goodby user!')

# Сделать 3 view (function based views)
# 1 - hello/ будет возвращать ответ HttResponse с текстом "Hello! Its my project"
# 2 - now_date/ будет возвращать ответ HttpResponse c нынешней датой
# 3 - goodby/ будет возвращать ответ HttpResponse с текстом “Goodby user!”
#
# отправить как GitHub репозиторий, имя репозитория будет таким “{first_name}_{last_name}_{group}”
#
