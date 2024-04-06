from django.db import models
from django.conf import settings
from RSS_Sources.models import *
import hashlib, requests, os

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

    def keywords_(self):
        API_TOKEN = os.getenv('HFHUB_API_TOKEN', None)
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        payload = self.description+' '+self.title
        response = requests.post("https://api-inference.huggingface.co/models/ilsilfverskiold/bart_keywords", headers=headers, json=payload)
        data = response.json()
        try:
            dt = data[0]['generated_text']
            print(dt)
            return dt
        except:
            return ''

    def md5hash(self):
        content = f"""{self.title}{self.description}{self.content}""".encode()
        hash_ = hashlib.md5(content).hexdigest()
        return hash_

    def __str__(self):
        return f"{self.source} - {self.title}"

    def save(self, *args, **kwargs):
        self.keywords = self.keywords_()
        #print(self.keywords_())
        return super().save(*args, **kwargs)
