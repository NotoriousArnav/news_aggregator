from django.db import models
from RSS_Sources.models import *

# Create your models here.
class Article(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=1024, blank=False)
    source = models.ForeignKey(Source, on_delete=models.PROTECT, default=Source.get_default_pk, blank=False, null=False)
    description = models.TextField(blank=False)
    content = models.TextField(blank=True, default='')
    link = models.CharField(max_length=4096, default='example.com')
    datetime = models.DateTimeField(blank=False, null=False, editable=True)
    keywords = models.TextField(blank=True, default='')

    def __str__(self):
        return f"{self.source} - {self.title}"
