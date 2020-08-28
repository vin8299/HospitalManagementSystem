from django.urls import path
from .views import *

app_name="Patients"
urlpatterns = [
				
				path("<int:inp_id>/p_update", patients_update, name="p_update"),
				path("<int:inp_id>/p_delete", patients_delete, name="p_delete"),
				path("<int:inp_id>/", patients_byId, name="p_byId"),
				path("p_new/", patients_new, name="p_new"),
				path("p_all/", patients_all, name = "p_all")
			  ]