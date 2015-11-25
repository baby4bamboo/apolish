from django.db import models
from django.utils import timezone
import datetime


class News(models.Model):
    title = models.CharField(max_length=50)
    pubtime = models.DateTimeField()
    content = models.TextField(max_length=10000)
    class Meta:
        db_table = 'news'
    def __unicode__(self):
        return self.title
