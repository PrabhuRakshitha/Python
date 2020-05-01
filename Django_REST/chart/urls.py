from django.urls import path

from . import views

app_name ='chart'

urlpatterns = [
    path('', views.index, name='index'),
    path('chart_data/<slug:country>', views.Chart_data.as_view()),
    path('chart_data_elastic/<slug:country>', views.Chart_data_elastic.as_view()),
]