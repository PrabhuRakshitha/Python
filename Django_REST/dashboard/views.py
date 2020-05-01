from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect , JsonResponse
from django.urls import reverse
# Create your views here.
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import ClusterSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from .models import Cluster

from elasticsearch import Elasticsearch


def create_index():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    clusters = Cluster.objects.all()
    for cluster in clusters:
        cluster_id = cluster.cluster_id
        serializer = ClusterSerializer(cluster)
        es.index(index='cluster-index', id=cluster_id, body=serializer.data)


def index(request):
    clusters = Cluster.objects.order_by('-cluster_id')
    context = {'clusters': clusters, }
    return render(request, 'dashboard/index.html', context)


def edit_cluster(request, cluster_id):
    cluster = Cluster.objects.filter(cluster_id=cluster_id)
    clusters = Cluster.objects.order_by('-cluster_id')
    context ={'clusters': clusters, 'cluster_id': cluster_id, }
    return render(request, 'dashboard/index.html', context)


def save_cluster(request, cluster_id):
    cluster = Cluster.objects.get(cluster_id=cluster_id)
    cluster.server_count = request.POST['count']
    cluster.save()
    return HttpResponseRedirect(reverse('dashboard:index'))

@api_view(['GET','POST'])
def dashboard_rest(request):
    if request.method == 'GET':
        cluster = Cluster.objects.all()
        serializer = ClusterSerializer(cluster, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClusterSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def dashboard_detail_rest(request, cluster_id):
    try:
        cluster = Cluster.objects.get(cluster_id=cluster_id)
    except Cluster.Does:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ClusterSerializer(cluster)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClusterSerializer( cluster,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        cluster.delete()
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


class ClusterList(APIView):
    def get(self,request):
        cluster = Cluster.objects.all()
        serializer = ClusterSerializer(cluster, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ClusterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ClusterElastic(APIView):
    def get(self,request):
        if es.indices.exists(index="cluster-index"):
            doc = {
                'size': 10000,
                'query': {
                    'match_all': {}
                }
            }
            temp =[]
            res = es.search(index="cluster-index", body=doc)
            for item in res["hits"]["hits"]:
                temp.append(item["_source"])
            context = {"clusters": temp}
            # return render(request, 'dashboard/index.html', context)
            return Response(context)
        else:
            create_index()

    def post(self, request):
        es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        cluster_id = request.data.cluster_id
        es.index(index='cluster-index', id=cluster_id, body=serializer.data)
        cluster = Cluster.objects.get(cluster_id=cluster_id)
        cluster.server_count = request.POST['count']
        cluster.save()
        return Response(context)
        # return HttpResponseRedirect(reverse('dashboard:Clusterelastic'))


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


def index_elastic(request):
    if not es.indices.exists(index="cluster-index"):
        create_index()
        # return Response(context)
    doc = {
        'size': 10000,
        'query': {
            'match_all': {}
        }
    }
    temp = []
    res = es.search(index="cluster-index", body=doc)
    for item in res["hits"]["hits"]:
        temp.append(item["_source"])
    context = {"clusters": temp}
    return render(request, 'dashboard/index_elastic.html', context)


def edit_cluster_elastic(request, cluster_id):
    doc = {
        'size': 10000,
        'query': {
            'match_all': {}
        }
    }
    temp = []
    res = es.search(index="cluster-index", body=doc)
    for item in res["hits"]["hits"]:
        temp.append(item["_source"])
    context = {"clusters": temp ,'cluster_id': cluster_id, }
    return render(request, 'dashboard/index_elastic.html', context)


def save_cluster_elastic(request, cluster_id):
    es.index(index='cluster-index', id=cluster_id, body=serializer.data)
    return HttpResponseRedirect(reverse('dashboard:index_elastic'))








