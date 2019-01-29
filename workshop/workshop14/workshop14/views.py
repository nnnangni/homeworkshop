from django.http import HttpResponse
from django.shortcuts import render
import random


def info(request):
    return render(request, "info.html")
    
def students(request,name):
    stu = {
        "박나원":25,
        "윤은솔":25,
        "강민지":28
    }
    age = stu.get(name)
    return render(request, "students.html",{"name":name,"age":age})