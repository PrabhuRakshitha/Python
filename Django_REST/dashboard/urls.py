from django.urls import path

from . import views

app_name='dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('cluster/<int:cluster_id>/', views.edit_cluster, name='edit_cluster'),
    path('cluster/<int:cluster_id>/save', views.save_cluster, name='save_cluster'),
    path('REST_API/', views.dashboard_rest, name='dashboard_rest'),
    path('detail/<int:cluster_id>', views.dashboard_detail_rest, name='dashboard_detail_rest'),
    path('cluster_list/', views.ClusterList.as_view(), name='ClusterList'),
    path('cluster_elastic_REST/', views.ClusterElastic.as_view(), name='Clusterelastic'),
    path('cluster_elastic/', views.index_elastic, name='index_elastic'),
    path('cluster_elastic/<int:cluster_id>/', views.edit_cluster_elastic, name='edit_cluster_elastic'),
    path('cluster_elastic/<int:cluster_id>/save', views.save_cluster, name='save_cluster_elastic'),

]