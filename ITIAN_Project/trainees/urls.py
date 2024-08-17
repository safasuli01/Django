from django.urls import path
from .views import *

urlpatterns = [
    path("", trainees_list, name="trainees_list"),
    path("Add/", create_trainee, name="create_trainee"),
    path("Update/<int:id>", update_traiee, name="update_traiee"),
    path("Delete/<int:id>", delete_trainee, name="delete_trainee"),
    path("Details/<int:id>", trainee_info, name="trainee_info"),
]