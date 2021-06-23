from django.urls import path, include
from .views import TriviaQuestionPage

urlpatterns = [
    path('/placebet', TriviaQuestionPage, name="place-bet"),
]