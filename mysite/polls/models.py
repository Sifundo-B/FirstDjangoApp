from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text


class Case(models.Model):
    case_number = models.IntegerField()
    title = models.CharField(max_length=200, help_text='Case Title')
    case_description = models.TextField(help_text='Case Description')
    city = models.CharField(max_length=200, help_text='Name of the City')
    province = models.CharField(max_length=200, help_text='Name of the Province')

    def __str__(self):
        return self.title
