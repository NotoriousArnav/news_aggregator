from django.shortcuts import render
from articles.models import Article
from django.shortcuts import get_object_or_404
# Create your views here.
def index(req):
    return render(req, 'index.html')

def article(req, slug):
    article = get_object_or_404(Article, slug=slug)
    context = {
        'slug': slug,
        'article': article,
    }
    return render(req, 'article.html', context=context)