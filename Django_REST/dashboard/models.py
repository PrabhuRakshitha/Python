from django.db import models

# Create your models here.


class Cluster(models.Model):
    cluster_id = models.AutoField(primary_key=True)
    cluster_name = models.CharField(max_length=100)
    server_count = models.IntegerField(default=0)