from django.urls import path
from . import views

app_name = "feedback"

urlpatterns = [
    path("", views.feedback_form, name="feedback_form"),
    path("success/", views.feedback_success, name="feedback_success"),
]
