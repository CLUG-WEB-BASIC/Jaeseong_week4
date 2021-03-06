from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length= 50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    hash_tag = models.CharField(max_length= 50, blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:10]