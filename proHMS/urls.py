"""proHMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import *
import Doctors.urls
import Patients.urls
from Users_Employees.views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hms/', mainpage, name='hms'),
    path('captcha/', include('captcha.urls')),
    path('home/', homepage, name="home"),
    path('signup/', SignUp, name='signup'),
    path('signin/', SignIn, name='signin'),
    path('signout/', SignOut, name='signout'),
    path('doctors/', include('Doctors.urls', namespace="Doctors")),
    path('patients/', include('Patients.urls', namespace="Patients"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
