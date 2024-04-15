from django.http import JsonResponse
from rest_framework import viewsets
from .models import Source, SourceType
from .serializers import *
from jobs import jobs

# Create your views here.
class SourceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed('POST')

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PUT')

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PATCH')

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed('DELETE')

class SourceTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SourceType.objects.all()
    serializer_class = SourceTypeSerializer

    def create(self, request, *args, **kwargs):
        raise MethodNotAllowed('POST')

    def update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PUT')

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PATCH')

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed('DELETE')

def update_sources(req):
    sources = Source.objects.all()
    updated = []
    errors = []
    code = 200
    for source in sources:
        try:
            jobs.get_feed(source)
            updated.append((source.name, source.rss_feed_link))
        except Exception as e:
            raise e
            errors.append((source.name, str(e.args)))
            code=500 


    return JsonResponse({
        'response': 'Success' if code==200 else 'Errors' ,
        'sources': {
                'errors': errors,
                'updated': updated
            }
        },
        status=code
    )

def make_update_articles(req):
    jobs.make_articles()
    jobs.update_keywords()
    return JsonResponse({})

def delete_cache_dupes(req):
    jobs.delete_cache()
    jobs.delete_dupes()
    return JsonResponse({})
