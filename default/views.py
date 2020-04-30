from django.shortcuts import render
from .models import Poll
from django.views.generic import ListView

# Create your views here.
def poll_list(req):
    polls = Poll.objects.all()
    return render(req, 'poll_list.html', {'poll_list':polls})

class PollList(ListView):
    model = Poll
