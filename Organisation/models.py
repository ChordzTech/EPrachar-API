from django.db import models

# Create your models here.
class Organisation(models.Model):
     org_name = models.CharField(max_length=200, blank=True, null=True)

     class Meta:
          db_table = 'organisation'
