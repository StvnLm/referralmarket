from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    applicants = models.ManyToManyField(User, related_name='appliedPosts', null=True)
    selectededApplicant = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='acceptedPosts', null=True)
    postId = models.IntegerField(primary_key=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    postDate = models.DateTimeField()
    requestPrice = models.IntegerField()
    requestTypeChoices = (
        ('WTB', 'Looking for referral'),
        ('WTS', 'Offering referral')
    )
    requestType = models.CharField(max_length=3, choices=requestTypeChoices)

