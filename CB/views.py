from django.shortcuts import render, HttpResponse, redirect
from .models import College, CollegeReview, CollegeQuestion, FollowCollege, UserDetails, QuestionAnswers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from datetime import date, datetime


def homepage(request):
    data = College.objects.values('college_name')
    li = []
    for i in range(len(data)):
        li.append(data[i]['college_name'])
    if request.user.is_authenticated is True:
        log = 0
    else:
        log = 1
    return render(request, 'homepage.html', {'list': li, 'log': log})


def auth(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        user = authenticate(request, username=name, password=password)
        if user is None:
            email = request.POST['email']
            User.objects.create_user(username=name, email=email, password=password)
            user = authenticate(request, username=name, password=password)
            login(request, user)

            return redirect("CB:Profile")

        else:
            login(request, user)
            return redirect("CB:Profile")

    return render(request, 'auth.html')


def profile(request):
    username = request.user.username
    id = request.user.id
    name = username[0].capitalize() + username[1:]
    try:
        coll_foll = FollowCollege.objects.filter(user=id)

    except FollowCollege.DoesNotExist:
        coll_foll = ''
    try:
        review = CollegeReview.objects.filter(user=id)
    except CollegeReview.DoesNotExist:
        review = ''
    try:
        question = CollegeQuestion.objects.filter(user=id)
    except CollegeQuestion.DoesNotExist:
        question = ''
    if request.user.is_authenticated is True:
        log = 0
    else:
        log = 1
    return render(request, 'profile.html',
                  {'username': name, 'log': log, 'collegefollowing': coll_foll, 'review': review,
                   "question": question})


def user_type(request):
    if request.method == 'POST':
        user = request.user
        usertype = request.POST['usertype']
        UserDetails.objects.create(user=user, user_type=usertype)
    return redirect('CB:Profile')


@login_required()
def college_page(request):
    global college, log, review, followers
    college = College.objects.get(college_name=request.GET['college'])

    try:
        review = CollegeReview.objects.filter(college=college)
    except CollegeReview.DoesNotExist:
        review = ''
    try:
        question = CollegeQuestion.objects.filter(college=college)
    except CollegeQuestion.DoesNotExist:
        question = ''
    try:
        answer = QuestionAnswers.objects.filter(college=college)
    except QuestionAnswers.DoesNotExist:
        answer = ''
    try:
        followers = FollowCollege.objects.filter(college__college_name=college)
    except FollowCollege.DoesNotExist:
        followers = ''
    if request.user.is_authenticated is True:
        log = 0
    else:
        log = 1
    return render(request, 'college_page.html', {'college': college, 'log': log, 'review': review,
                                                 "question": question, 'answer': answer, 'followers': followers.count()})


def add_connection(request):
    return 1


def ask_question(request):
    if request.method == 'POST':
        question = request.POST['question']
        college = College.objects.get(college_name=request.POST['college'])
        user = request.user
        CollegeQuestion.objects.create(college=college, user=user, question=question, time=datetime.now())
        return redirect('/college_page?college=%s' % college)


def answer_question(request):
    if request.method == 'POST':
        answer = request.POST['answer']
        college = College.objects.get(college_name=request.POST['college'])
        question = CollegeQuestion.objects.get(question=request.POST['question'])
        user = request.user
        QuestionAnswers.objects.create(user=user, question=question, college=college, answer=answer,
                                       time=datetime.now())
        return redirect('/college_page?college=%s' % college)


def write_review(request):
    if request.method == 'POST':
        review = request.POST['review']
        college = College.objects.get(college_name=request.POST['college'])
        user = request.user
        CollegeReview.objects.create(college=college, user=user, review=review, time=datetime.now())
        return redirect('/college_page?college=%s' % college)
    return 1


def follow_college(request):
    if request.method == 'POST':
        user = request.user
        coll = request.POST['college']
        college = College.objects.get(college_name=coll)
        FollowCollege.objects.create(user=user, college=college)
    return redirect('/college_page?college=%s' % college)
