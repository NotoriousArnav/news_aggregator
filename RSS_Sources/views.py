from django.shortcuts import render
from rest_framework import serializers, viewsets, routers
from .models import Source, SourceType
from .serializers import *

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
