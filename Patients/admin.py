from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
	list_display = [
					"id",
					"p_name",
					"p_address",
					"disease",
					"contact_no",
					"ward_no",
					"timestamp",
				   ]
	list_display_links = [
							"p_name"
						 ]
	list_filter = [
					"timestamp"
					]
	search_fields = [ "p_name "]

admin.site.register(Patient,PatientAdmin)