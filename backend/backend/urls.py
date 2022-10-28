from django.contrib import admin
from django.urls import path,include               
from rest_framework import routers                 
from Customers import views                             

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerView, 'customers')  


urlpatterns = [
    path('admin/', admin.site.urls),
    path('funk_tion/', views.funk_tion),
    path('make_match/', views.make_match)
]
urlpatterns += router.urls