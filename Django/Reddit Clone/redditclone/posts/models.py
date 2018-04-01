from django.conf import settings
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)
    votes_total = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    def pub_date_formatted(self):
        return self.pub_date.strftime('%b %e, %Y')
