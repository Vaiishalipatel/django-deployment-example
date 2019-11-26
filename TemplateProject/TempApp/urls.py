from django.conf.urls import url
from TempApp import views

app_name = "TempApp"

urlpatterns = [
        url(r'^relative/$',views.relative,name="relative"),
        url(r'^other/$',views.other,name="other")
]
