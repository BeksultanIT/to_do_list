from django.http import HttpResponseRedirect
from django.shortcuts import render

from webapp.models import Article, status_choices


# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'index.htm', {'articles': articles})

def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        Article.objects.create(title=title, status=status, deadline=deadline)
        return HttpResponseRedirect("/")
    else:
        return render(request, 'new.html', {'status_choices': status_choices})
