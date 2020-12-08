from django.shortcuts import render
from rest_framework import viewsets
from .models import Basic
from .serializers import BasicSerializer


class BasicView(viewsets.ModelViewSet):
    queryset = Basic.objects.all()
    serializer_class = BasicSerializer


b = Basic.objects.latest('id')

norm_vlaznost = 60


# Алгоритм для определения состояния почвы относительно валажности
def vlazhnost_stats(norm_vlaznost_func, vlazhnost_func):
    if vlazhnost_func - norm_vlaznost_func >= 15:
        if 15 <= vlazhnost_func - norm_vlaznost_func < 40:
            return 'Необходимо осушить почву'
        elif 40 <= vlazhnost_func - norm_vlaznost_func < 60:
            return 'Переизбыток воды, срочно осушите почву'
        elif vlazhnost_func - norm_vlaznost_func >= 60:
            return 'В почве крайне высокий переизбыток воды, осушить немедленно'
    elif vlazhnost_func - norm_vlaznost_func <= -15:
        if -15 >= vlazhnost_func - norm_vlaznost_func > -40:
            return 'Необходимо полить почву'
        elif -40 >= vlazhnost_func - norm_vlaznost_func > -60:
            return 'Недостаток воды, срочно полейте почву'
        elif vlazhnost_func - norm_vlaznost_func <= -60:
            return 'Крайне высокая нехватка воды, полить немедленно'
    else:
        return 'Состояние влажности почвы в норме'


norm_temp = 25


# Алгоритм для определения состояния почвы относительно температуры
def tempr_stats(norm_temp1, temp1):
    if temp1 - norm_temp1 >= 15:
        return 'Температура почвы высокая'
    elif temp1 - norm_temp1 <= -10:
        return 'Температура почвы низкая'
    else:
        return 'Температура в норме'


def analyze(request):
    b = Basic.objects.latest('id')
    vlazhnost = int(b.moist)
    temp = int(b.temp)
    result_vlazhnost = vlazhnost_stats(norm_vlaznost, vlazhnost)
    result_temp = tempr_stats(norm_temp, temp)

    return render(request, 'analyze/analyze.html',
                  context={'temp_func': result_temp, 'moisture': result_vlazhnost, 'vlazhnost': vlazhnost,
                           'temperatura': temp})
