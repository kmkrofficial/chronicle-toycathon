from django.shortcuts import render


# Create your views here.
def TriviaQuestionPage(request):



    return render(request, "quiz.html")