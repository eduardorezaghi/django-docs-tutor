import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    """Model representing a question"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        """Method returning a True of False assertion depending
        if the question was published recently"""
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self) -> str:
        return str(self.question_text)

class Choice(models.Model):
    """Model representing a choice"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return str(self.choice_text)