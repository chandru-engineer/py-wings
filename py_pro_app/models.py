from django.db import models

# Create your models here.


class Topics(models.Model):
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True)
    code_json = models.FileField(null=True)

    def __str__(self):
        return self.title
