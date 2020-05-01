from rest_framework import serializers

from .models import Cluster


class ClusterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cluster
        fields = ['cluster_id','cluster_name', 'server_count']

