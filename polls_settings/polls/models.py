from django.db import models
from django.utils import timezone
import datetime
from django.urls import reverse
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200,help_text='ques')
    pub_date = models.DateTimeField('date published',help_text='yyyy-mm-dd')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now- datetime.timedelta(days=1)<=self.pub_date <= now
        # return self.pub_date >= now - datetime.timedelta(days=1)

        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'
        # def get_absolute_url(self):
        #     return reverse('polls:detail',kwargs={'pk':self.pk})

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age= models.IntegerField(help_text='your age')
    dob= models.DateField('dob',help_text='yyyy/mm/dd')
    def __str__(self):
        return self.user.username

class Publication(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        ordering = ('-title',)

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
    class Meta:
        ordering = ('-headline',)
    def __str__(self):
        return self.headline
