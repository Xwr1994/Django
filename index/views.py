from django.shortcuts import render
from choujiang.models import People
from choujiang.models import People_first
from choujiang.models import People_second
from choujiang.models import People_third
# Create your views here.


def init():
    if (People_first.objects.all().count() != 0):
        People_first.objects.all()[0].delete()
    if (People_second.objects.all().count() != 0):
        for x in range(0, People_second.objects.all().count()):
            People_second.objects.all()[x].delete()
    if (People_third.objects.all().count() != 0):
        print(People_third.objects.all().count())
        for x in range(0, People_third.objects.all().count()):
            People_third.objects.all()[x].delete()
    for i in range(1, 11):
        People.objects.get_or_create(name="test"+str(i), english_name="en_name"+str(i), card_id=i)


def index(request):
    init()
    return render(request, 'index/index.html')


