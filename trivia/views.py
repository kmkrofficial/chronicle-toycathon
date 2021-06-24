from django.shortcuts import redirect, render
from .models import Category, Questionnaire, Score
import random


# Create your views here.
def index(request):
    return render(request, 'trivia/index.html', {})


def TriviaQuestionPage(request):
    upScore, created = Score.objects.get_or_create(user__pk=request.user.id,
                                                   user=request.user)

    return render(request, "trivia/Betting.html", {'score': upScore})


def start(request):
    request.session['categories'] = 0
    return render(request, "trivia/start_page.html")


def leaderboard(request):
    top = Score.objects.all().order_by('-score')

    return render(request, "trivia/leaderboard.html", {'scores': top})


def categories(request):
    if 'categories' in request.session:
        curr_category = request.session.get('categories')
        curr_category = curr_category + 1
        request.session['categories'] = curr_category
    else:
        request.session['categories'] = 1

    categories = request.session['categories']
    count = Category.objects.all().count()
    if (categories > count):
        request.session['categories'] = 0
        # catObj = Category.objects.get(pk=(count))
        # quiz = Questionnaire.objects.filter(category__pk=catObj.id)
        # print(quiz)
        # quizlis = []
        # for i in quiz:
        #     quizlis.append(i.id)

        # print(quizlis)
        # random.shuffle(quizlis)
        # request.session['quizes'] = quizlis

        return redirect(leaderboard)
    catObj = Category.objects.get(pk=categories)
    quiz = Questionnaire.objects.filter(category__pk=catObj.id)
    print(quiz)
    quizlis = []
    for i in quiz:
        quizlis.append(i.id)

    print("wpw", quizlis)
    random.shuffle(quizlis)
    request.session['quizes'] = quizlis

    return render(request, "trivia/video.html", {'cat': catObj})


def quiz1(request):
    temp = request.GET.get('bidding')
    if (temp):
        request.session['bid'] = temp
    points = int(request.session.get('bid'))
    print(points)
    if (request.GET.get('qid')):
        if (request.GET['answer'] == request.GET['crt']):
            upScore, created = Score.objects.get_or_create(
                user__pk=request.user.id, user=request.user)
            upScore.score = upScore.score + points
            print(upScore.score)
            upScore.save()
        else:
            upScore, created = Score.objects.get_or_create(
                user__pk=request.user.id, user=request.user)

            upScore.score = int(upScore.score) - points
            if (upScore.score < 0):
                upScore.score = 0
            upScore.save()

    quizes = request.session.get('quizes')
    if (len(quizes) == 0):
        return redirect(categories)
    quiz_id = quizes[len(quizes) - 1]
    quizes.pop()
    request.session['quizes'] = quizes
    quizObj = Questionnaire.objects.get(pk=quiz_id)

    return render(request, "trivia/quiz1_page.html", {'quizObj': quizObj})
