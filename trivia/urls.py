from django.urls import path, include
from .views import TriviaQuestionPage, index, categories, quiz1, start, leaderboard

urlpatterns = [
    path('placebet', TriviaQuestionPage, name="place-bet"),
    path('categories', categories, name="categories"),
    path('start', start, name="start"),
    path('quiz1', quiz1, name="quiz1"),
    path('leaderboard', leaderboard, name='lb'),
    path('', index, name="index"),
]
