from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('마감기한')
    body = models.TextField()

    def __str__(self):
        return self.title


class File(models.Model):
    title = models.CharField(max_length=1000)
    subject = models.CharField(max_length=20)
    body = models.TextField()

    def __str__(self):
        return self.title