from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class College(models.Model):
    OWNED_TYPES = (
        ('C', 'Central University'),
        ('D', 'Deemed University'),
        ('P', 'Private University'),
    )
    college_name = models.CharField(max_length=10000, unique=True)
    location = models.CharField(max_length=500)
    year = models.PositiveIntegerField(default='')
    specialization = models.CharField(max_length=500)
    owned = models.CharField(choices=OWNED_TYPES, max_length=50, default='')

    def __str__(self):
        return self.college_name


class UserDetails(models.Model):
    USER_TYPE_CHOICES = (
        ('CS', 'College Student'),
        ('F', 'Faculty'),
        ('CAS', 'College Aspirant'),
        ('O', 'Others'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college = models.ForeignKey(College, to_field='college_name', on_delete=models.CASCADE, default='', blank=True)
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)


class CollegeReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college = models.ForeignKey(College, to_field='college_name', on_delete=models.CASCADE)
    review = models.CharField(default='', max_length=500)
    time = models.DateTimeField(default='')


class CollegeQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college = models.ForeignKey(College, to_field='college_name', on_delete=models.CASCADE)
    question = models.CharField(default='', max_length=500, unique=True)
    time = models.DateTimeField(default='')

    def __str__(self):
        return self.question


class QuestionAnswers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(CollegeQuestion, to_field='question', on_delete=models.CASCADE)
    college = models.ForeignKey(College, to_field='college_name', on_delete=models.CASCADE)
    answer = models.CharField(default='', max_length=1000, blank=True)
    time = models.DateTimeField(default='')

    def __str__(self):
        return self.answer


class FollowCollege(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college = models.ForeignKey(College, to_field='college_name', on_delete=models.CASCADE)

    def __str__(self):
        return self.college_id
