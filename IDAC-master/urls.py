from IDACapp1 import views
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "IDAC Admin"
admin.site.site_title = "IDAC Admin Portal"
admin.site.index_title = "Welcome to IDAC Administrator Portal"

urlpatterns = [
    path('', views.index,name = 'home' ),
    path('explore', views.explore, name='explore'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('signup', views.register, name='signup'),
    path('login', views.login, name='login'),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
  
 ]
 
 
