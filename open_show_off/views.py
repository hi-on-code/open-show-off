from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import TemplateView

# @login_required
# def home(request):
#     return render(request, 'home.html')

@login_required
def home(request, *args, **kwargs):
    return render(request, 'index.html', context=None)
