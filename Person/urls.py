from .views import PersonView, PersonViewById
from django.urls import path

urlpatterns = [
    path("person_view/", PersonView.as_view()),
    path("person_by_id/<int:pk>/", PersonViewById.as_view()),
]