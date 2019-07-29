from django.urls import path

from . import views

app_name='cmpdetails'

urlpatterns = [
    path('', views.index, name='index'),
    path('cmp_details/', views.cmp_details , name='cmp_details'),
    path('<int:comp_id>/',views.emp_details, name='emp_details'),
    path('<int:comp_id>/<int:emp_id>/',views.emp_delete, name='emp_delete'),
    path('<int:comp_id>/<int:emp_id>/emp_update',views.emp_update, name='emp_update'),
    path('<int:emp_id>/emp_update',views.emp_update_save, name='emp_update_save'),
    path('cmp_details/<int:comp_id>/add_new_emp_pg',views.add_new_emp_pg,name='add_new_emp_pg'),
    path('cmp_details/<int:comp_id>/emp_add_new',views.emp_add_new,name='emp_add_new'),
]