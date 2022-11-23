from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from app.aws import creatInstance
import json
# Create your models here.
class AwsInstance(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    instance_name = models.CharField(blank=True,null=True,max_length=300)
    creation_time = models.DateTimeField(default=timezone.now)
    expiry_time= models.DateTimeField(blank=False,null=False)
    data = models.JSONField(blank=True,null=True)

    def save(self) -> None:
        data = creatInstance()
        serialize = {"id":data[0].id}
        self.data = serialize
        return super().save()
    

    def __str__(self) -> str:
        return self.instance_name