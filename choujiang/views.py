from django.shortcuts import render
import random
from choujiang.models import People
from choujiang.models import People_first
from choujiang.models import People_second
from choujiang.models import People_third

# Create your views here.


def choujiang_1(request):
    return render(request, 'choujiang/1.html')


def choujiang_2(request):
    return render(request, 'choujiang/2.html')


def choujiang_3(request):
    return render(request, 'choujiang/3.html')


def result_1(request):
    x = People.objects.all()
    y = x.__len__()
    select_list = random.sample(range(0, y), 1)
    print(select_list)
    People_1 = list()
    for a in select_list:
        name = People.objects.all()[a].name
        People_1.append(name)
        english_name = People.objects.all()[a].english_name
        People_1.append(english_name)
        card_id = People.objects.all()[a].card_id
        People_1.append(card_id)
        People_first.objects.get_or_create(name=name, english_name=english_name, card_id=card_id)
    People.objects.filter(name=name).delete()
    return render(request, 'choujiang/result_1.html', {'People_1': People_1})


def result_2(request):
    x = People.objects.all()
    y = x.__len__()
    select_list = random.sample(range(0, y), 3)
    print(select_list)
    Peoples = list()
    for a in select_list:
        name = People.objects.all()[a].name
        Peoples.append(name)
        english_name = People.objects.all()[a].english_name
        Peoples.append(english_name)
        card_id = People.objects.all()[a].card_id
        Peoples.append(card_id)
        People_second.objects.get_or_create(name=name, english_name=english_name, card_id=card_id)
    People.objects.filter(name=Peoples[0]).delete()
    People.objects.filter(name=Peoples[3]).delete()
    People.objects.filter(name=Peoples[6]).delete()
    People_1 = Peoples[0:3]
    People_2 = Peoples[3:6]
    People_3 = Peoples[6:9]
    return render(request, 'choujiang/result_2.html', {'People_1': People_1, 'People_2': People_2, 'People_3': People_3})


def result_3(request):
    x = People.objects.all()
    y = x.__len__()
    select_list = random.sample(range(0, y), 6)
    print(select_list)
    Peoples = list()
    for a in select_list:
        name = People.objects.all()[a].name
        Peoples.append(name)
        english_name = People.objects.all()[a].english_name
        Peoples.append(english_name)
        card_id = People.objects.all()[a].card_id
        Peoples.append(card_id)
        People_third.objects.get_or_create(name=name, english_name=english_name, card_id=card_id)
    People.objects.filter(name=Peoples[0]).delete()
    People.objects.filter(name=Peoples[3]).delete()
    People.objects.filter(name=Peoples[6]).delete()
    People.objects.filter(name=Peoples[9]).delete()
    People.objects.filter(name=Peoples[12]).delete()
    People.objects.filter(name=Peoples[15]).delete()
    People_1 = Peoples[0:3]
    People_2 = Peoples[3:6]
    People_3 = Peoples[6:9]
    People_4 = Peoples[9:12]
    People_5 = Peoples[12:15]
    People_6 = Peoples[15:18]
    return render(request, 'choujiang/result_3.html',
                  {'People_1': People_1, 'People_2': People_2, 'People_3': People_3, 'People_4': People_4, 'People_5': People_5, 'People_6': People_6})


def result_all(request):
    Peoples_1 = list()
    Peoples_2 = list()
    Peoples_3 = list()
    Peoples_1.append(People_first.objects.all()[0].name)
    Peoples_1.append(People_first.objects.all()[0].english_name)
    Peoples_1.append(People_first.objects.all()[0].card_id)
    for x in range(0, 3):
        Peoples_2.append(People_second.objects.all()[x].name)
        Peoples_2.append(People_second.objects.all()[x].english_name)
        Peoples_2.append(People_second.objects.all()[x].card_id)
    for x in range(0, 6):
        Peoples_3.append(People_third.objects.all()[x].name)
        Peoples_3.append(People_third.objects.all()[x].english_name)
        Peoples_3.append(People_third.objects.all()[x].card_id)
    People_11 = Peoples_1
    People_21 = Peoples_2[0:3]
    People_22 = Peoples_2[3:6]
    People_23 = Peoples_2[6:9]
    People_31 = Peoples_3[0:3]
    People_32 = Peoples_3[3:6]
    People_33 = Peoples_3[6:9]
    People_34 = Peoples_3[9:12]
    People_35 = Peoples_3[12:15]
    People_36 = Peoples_3[15:18]
    return render(request, 'choujiang/result_all.html',
                  {'People_11': People_11, 'People_21': People_21, 'People_22': People_22, 'People_23': People_23,
                   'People_31': People_31, 'People_32': People_32, 'People_33': People_33, 'People_34': People_34, 'People_35': People_35, 'People_36': People_36})

