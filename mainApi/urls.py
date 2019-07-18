from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import bankDetails

urlpatterns = [
    path('branches', bankDetails.as_view()),
    path('bankDetail', views.bankDetail, name="bankDetail")
]
urlpatterns = format_suffix_patterns(urlpatterns)