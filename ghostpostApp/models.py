from django.db import models
from django.utils import timezone


class ghostpost(models.Model):
    ghostpost_choice = models.BooleanField(
        choices=[(True, 'Boast'), (False, 'Roast')])
    ghostpost_content = models.CharField(
        max_length=280, verbose_name='Content')
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ghostpost_content
