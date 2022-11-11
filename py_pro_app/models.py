from django.db import models

# Create your models here.


class Topics(models.Model):
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Question(models.Model):

    DEFICULT_LEVEL = (
    ("Easy", "easy"),
    ("Medium", "medium"),
    ("Hard", "hard"),

)

    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    ques = models.CharField(max_length=200)
    describ = models.TextField(null=True)
    code = models.TextField(null=True)
    deficult_level = models.CharField(max_length=20, choices=DEFICULT_LEVEL, default = '1')
    answer = models.TextField(null=True)
    added = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-added',)

    def __str__(self):
        return self.ques