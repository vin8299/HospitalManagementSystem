from django.urls import path
from django.shortcuts import render,Http404,redirect




def mainpage(request):
	context = {
				"title": "Hospital Management System"
		      }
	return render(request, "outlayout.html", context)

def homepage(request):
	if not request.user.is_authenticated:
		return redirect('signin')
	context = {
				"title":"Hospital Management Syatem",
				}
	return render(request, "homepage.html", context)