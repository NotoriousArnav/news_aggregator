from django.shortcuts import render, HttpResponse
from articles.models import Article
from django.shortcuts import get_object_or_404
from django.views.decorators.clickjacking import xframe_options_exempt
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

@xframe_options_exempt
def article_only_content(req, slug):
    article = get_object_or_404(Article, slug=slug)
    style = """
<style>
img {
    width: 75%;
}
</style>
    """
    data = f"""
<html>
<head>
{style}
</head>
<body>
{article.content}
</body>
</html>
    """
    return HttpResponse(data)