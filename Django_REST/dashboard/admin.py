from django.contrib import admin

# Register your models here.
from .models import Cluster


class ClusterAdmin(admin.ModelAdmin):
    model = Cluster
    extra = 1
    list_display = ('cluster_name', 'server_count')


admin.site.register(Cluster, ClusterAdmin)