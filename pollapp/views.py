from django.shortcuts import render


# Create your views here.

def home(request):
    context = {}
    return render(request, 'home.html', context)


def create(request):
    context = {}
    return render(request, 'create.html', context)


def vote(request, poll_id):
    context = {}
    return render(request, 'vote.html', context)


def results(request, poll_id):
    context = {}
    return render(request, 'results.html', context)
