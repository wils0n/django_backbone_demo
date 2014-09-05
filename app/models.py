
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User 

from tastypie.utils.timezone import now


class Entry(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title