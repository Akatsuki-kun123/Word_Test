from unittest import result
from django.shortcuts import render
from django.http import HttpResponse
from .models import Unit
# Create your views here.

def index(request):
    admin_name = "ABC"
    _input = {"name" : admin_name}
    return render(request, 'Home/Home.html', _input)

def viewUnit(request):
    list_unit = Unit.objects.all()
    _input = {"Unit": list_unit}
    return render(request, 'Home/Unit_list.html', _input)

def viewDetails(request, unit_id):
    unit = Unit.objects.get(pk=unit_id)
    ques_id = 0
    if request.method == "POST":
        while (True):
            try:
                ques = unit.question_set.all()[ques_id]
                ques.answer_text = request.POST.get(str(ques.id))
                ques.save()
                ques_id = ques_id + 1
            except:
                return viewResult(request, unit_id)
    _input = {"Unit_details": unit, "Ques" : unit.question_set.all()}
    return render(request, 'Home/Details.html', _input)

def viewResult(request, unit_id):
    unit = Unit.objects.get(pk=unit_id)
    result = unit.question_set.all()
    _input = {"Result": result}
    return render(request, 'Home/Result.html', _input)