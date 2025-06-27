from django.shortcuts import render, redirect, get_object_or_404

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
        content = request.POST.get('content')
        article = Article.objects.create(title=title, status=status, deadline=deadline, content=content)
        return redirect('detail_article', pk=article.id)
    else:
        return render(request, 'new.html', {'status_choices': status_choices})

def detail_article(request,*args,pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'detail_article.html', {'article': article})
