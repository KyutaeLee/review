from django.shortcuts import render
from django.http import HttpResponse

from practice.models import Candidate

# Create your views here.

def Prac(request):
    candidates = Candidate.objects.all()
    return render(request, 'practice/index.html', {'candidates':candidates})





