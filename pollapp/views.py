from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Poll
from .forms import CreatePollForm
from django.http import JsonResponse


# Create your views here.

def home(request):
    poll = Poll.objects.all()
    context = {'poll': poll}
    return render(request, 'home.html', context)


def create(request):
    form = CreatePollForm()
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'create.html', {'form': form})


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(404, 'Invalid Form')
        poll.save()
        # print(request.POST['poll'])
        return HttpResponseRedirect('/results/%s' % poll_id)
        # if request.POST['poll']
    else:
        context = {'poll': poll}
        return render(request, 'vote.html', context)


def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {'poll': poll}
    return render(request, 'results.html', context)


def jsonresults(request, poll_id):
    polllist = []
    poll = Poll.objects.get(pk=poll_id)
    polllist.append({poll.option_one: poll.option_one_count})
    polllist.append({poll.option_two: poll.option_two_count})
    polllist.append({poll.option_three: poll.option_three_count})
    print(polllist)
    return JsonResponse(polllist, safe=False)

    # context = {'poll': poll}
    # return render(request, 'results.html', context)
