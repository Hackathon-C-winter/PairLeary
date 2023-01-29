
# f,rom email.policy import default
from django.db import models
from django.contrib.auth.models import User

    
class Content(models.Model):
    condition_id = models.IntegerField(primary_key=True)
    user_id = models.CharField(default='null',max_length=255)
    category = models.CharField(default='null',max_length=255)
    comment = models.CharField(default='null',max_length=255)


    def __str__(self):
        return self.title

class Conditions(models.Model):
    condition_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey("User", to_field='id', null=True)
    category = models.CharField(default='null', max_length=150)
    comment = models.CharField(default='null', max_length=255)

    def __str__(self):
        return self.condition_id

