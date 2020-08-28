from django.urls import path
from .views import *

app_name = "Doctors"

urlpatterns = [
    path("<str:inp_user>/info", doctors_user, name="d_user"),
    path('appoint/', doctors_appoint, name="appoint"),
    path('<int:inp_id>/d_update', doctors_update, name="d_update"),
    path('<int:inp_id>/', doctors_byId, name="d_byId"),
    path("d_new/", doctors_new, name="d_new"),
    path("d_all/", doctors_all, name="d_all")
]
