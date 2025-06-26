from django.shortcuts import render

from webapp.models import Article


# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'index.htm', {'articles': articles})


