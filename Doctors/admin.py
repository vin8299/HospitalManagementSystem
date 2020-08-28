from django.contrib import admin

from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
	list_display = [	"id",
						"d_name",
						"d_address",
						"image",
						"speciality",
						"contact_no",
						"timestamp",
					]
	list_display_links = [
							"d_name"
						]
	list_filter = ["timestamp"]

	search_fields = [ "speciality" ]

admin.site.register(Doctor, DoctorAdmin)