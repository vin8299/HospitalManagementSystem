from django.shortcuts import render, redirect, Http404, get_object_or_404
from .models import Doctor
from .forms import DoctorForm
from Patients.forms import PatientForm


def doctors_appoint(request):
    if not request.user.is_authenticated:
        raise Http404("Login required!!")
    form = PatientForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("Patients:p_all")
    context = {
        "title": "Get Appointment",
        "form": form
    }
    return render(request, "doctors_appoint.html", context)


def doctors_update(request, inp_id):
    if not request.user.is_authenticated:
        raise Http404("Login required!!")
    doctor = get_object_or_404(Doctor, id=inp_id)
    form = DoctorForm(request.POST or None, instance=doctor)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("Doctors: d_all")

    context = {
        "title": "Update details",
        'form': form
    }
    return render(request, "doctors_update.html", context)


def doctors_byId(request, inp_id):
    if not request.user.is_authenticated:
        raise Http404("Login required!!")
    doctor = get_object_or_404(Doctor, id=inp_id)

    context = {
        "title": "Details",
        "doctor": doctor
    }
    return render(request, "doctors_byId.html", context)


def doctors_new(request):
    if not request.user.is_authenticated:
        raise Http404("Login required!!")
    form = DoctorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect("Doctors:d_all")

    context = {
        "title": "Add Doctor",
        "form": form
    }
    return render(request, "doctors_new.html", context)


def doctors_user(request, inp_user):
    if not request.user.is_authenticated:
        raise Http404("login required")
    u_doctors = Doctor.objects.all()
    u_doctors = u_doctors.filter(user__username=inp_user)
    print(u_doctors)
    if not u_doctors:
        raise Http404("Available does not exist!!")

    search_q = request.GET.get("search")
    if search_q:
        u_doctors = u_doctors.filter(speciality__icontains=search_q)
    context = {
        "title": "All Doctors",
        "doctors": u_doctors
    }
    return render(request, "doctors_user.html", context)


def doctors_all(request):
    if not request.user.is_authenticated:
        raise Http404("Login required!!")
    doctors = Doctor.objects.all()

    search_q = request.GET.get("search")
    if search_q:
        doctors = doctors.filter(speciality__icontains=search_q)

    context = {
        "title": "All Doctors",
        "doctors": doctors
    }

    return render(request, "doctors_all.html", context)
