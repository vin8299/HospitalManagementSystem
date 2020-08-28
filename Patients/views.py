from django.shortcuts import render, redirect, Http404, render, get_object_or_404
from .models import Patient
from .forms import PatientForm


def patients_delete(request, inp_id):
	if not request.user.is_authenticated:
		redirect("signin")
	patient = get_object_or_404(Patient, id=inp_id)
	patient.delete()
	context ={
			  "title":"Deleted",
			  "heading":"Deleted Successfully!!"
			}
	return render(request, "patients_delete.html", context)

def patients_update(request, inp_id):
	if not request.user.is_authenticated:
		raise Http404("Login required!!!")
	patient = get_object_or_404(Patient, id=inp_id)
	form = PatientForm(request.POST or None, instance=patient)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		return redirect("Patients:p_all")
	context = {
				"title":"Update details",
				"form":form
			  }
	return render(request, "patients_update.html", context)

def patients_byId(request, inp_id):
	if not request.user.is_authenticated:
		raise Http404("Login required!!!")
	patient = get_object_or_404(Patient, id=inp_id)

def patients_new(request):
	if not request.user.is_authenticated:
		raise Http404("Login required!!!")
	form = PatientForm(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return redirect("Patients:p_all")
	context = {
				"title":"Add Patient",
				"form":form
			  }
	return render(request, "patients_new.html", context)

'''def patients_user(request, inp_user):
	if not request.user.is_authenticated:
		raise Http404("Login required!!!")
	patients = Patient.objects.all()
	patients.filter(user__username=inp_user)

	if not patients:
		raise Http404("User does not exist!!")
	
	search_q = request.GET.get("search")
	if search_q: 
		patients = patients.filter(p_name__icontains=search_q)


	context = {
				"title":"All Patients",
				"patients":patients
	}
	return render(request, "patients_user.html", context)'''	


def patients_all(request):
	if not request.user.is_authenticated:
		raise Http404("Login required!!!")
	patients = Patient.objects.all()

	q_search = request.GET.get("search")
	if q_search:
		patients = patients.filter(p_name__icontains=q_search)

	context = {
				"title":"All patients",
				"patients":patients
			  }
	return render(request, "patients_all.html", context)
