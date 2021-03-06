from tkinter import CASCADE
from unicodedata import name
from django.db import models

class Poll(models.Model):
    name = models.CharField(max_length= 256)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "{0} (Slug: {1})".format(self.name, self.slug)

class Choice(models.Model):
    poll = models.ForeignKey(to='Poll', on_delete=models.CASCADE)
    name = models.CharField(max_length= 256)
    votes = models.IntegerField(default=0)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{0}: {1}".format(self.poll.name, self.name)

# Choice.objects.filter(poll__id=1).all()     dasselbe wie: a.choice_set.all()