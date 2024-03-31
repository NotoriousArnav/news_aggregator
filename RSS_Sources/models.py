from django.db import models
import uuid

# Create your models here.
class SourceType(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 
    name = models.CharField(max_length=256)
    SOURCE = (
        ('Video', 'Video'),
        ('audio_pod', 'Audio Podcast'),
        ('video_pod', 'Video Podcast'),
        ('text', 'Text Article'),
        ('smp', 'Social Media Post'),
        ('oth', 'Others')
    )
    source_type = models.CharField(max_length=10, choices=SOURCE, default='oth')

    @classmethod
    def get_default_pk(cls):
        stype, created = cls.objects.get_or_create(
            name = "Others"
        )
        return stype.pk

    def __str__(self):
        return self.name


class Source(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default = uuid.uuid4,
        editable = False
    )
    name = models.CharField(max_length=512)
    favicon = models.CharField(max_length=2048, blank=True, null=True)
    rss_feed_link = models.CharField(max_length=4096, null=False, blank=False)
    date_added = models.DateField(auto_now_add=True, blank=False)
    type = models.ForeignKey(SourceType, on_delete=models.RESTRICT, default=SourceType.get_default_pk)

    @classmethod
    def get_default_pk(cls):
        obj, created = cls.objects.get_or_create(
            name = "Others",
            rss_feed_link= "https://example.com/"
        )
        return obj.pk

    def __str__(self):
        return self.name

class RSS_Cache(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default = uuid.uuid4,
        editable = False
    )
    source = models.ForeignKey(Source, on_delete=models.PROTECT, default=Source.get_default_pk)
    cache = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=False)