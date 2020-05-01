from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect , JsonResponse
from django.urls import reverse

# Create your views here.
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from rest_framework import serializers
import pandas as pd

from elasticsearch import Elasticsearch

def load_data():
    csv_file = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    try:
        covid_global = pd.read_csv(csv_file)
    except Others:
        error_message = 'Not able to load file'

    covid_global.drop(['Province/State', 'Lat', 'Long'], axis=1, inplace=True)
    covid_global_summary = covid_global.groupby('Country/Region').sum()
    return covid_global_summary



def index(request):
    context = dict()
    covid_sum =load_data()
    context['countries'] =list(covid_sum.index)
    return render(request, 'chart/chart.html', context)


class Chart_data(APIView):
    def get(self, request,country='US'):
        covid_global_summary =load_data()
        country = country.replace('_', ' ')
        serialized_data = covid_global_summary.loc[country].to_dict()
        data ={ 'computers':10, 'laptop':20, 'mouse': 5}
        return Response(serialized_data)


class Chart_data_elastic(APIView):
    def get(self, request,country='US'):
        es_obj = Elasticsearch([{'host': 'localhost', 'port': 9200}])
        if es_obj:
            print("connected to elastic search")
        else:
            print('some error')
        country = country.replace('_', ' ')
        res = es_obj.get(index="covid19", id=country)
        return Response(res['_source'])









