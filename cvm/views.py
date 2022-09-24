from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import pdfkit
from django_pdfkit import PDFView
from .models import CV
import io
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib.auth.models import User
from .models import Education, Experience
import os
from django.conf import settings

def cvmake(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        data = dict(request.POST)
        name = data.get('name')[0]
        email = data.get('email')[0]
        phone = data.get('phone')[0]
        skills = data.get('skills')[0]
        about = data.get('about')[0]
        interests = data.get('interests')[0]
        new_cv = CV(skills=skills, name=name, email=email, phone=phone, about=about, interests=interests)
        new_cv.save()
        request.user.cv.add(new_cv)
        college = list(data.get('college'))
        degree = data.get('degree')
        score = data.get('score')
        col_dur = data.get('col-duration')
        comp = data.get('company')
        work = data.get('work')
        position = data.get('position')
        exp_dur = data.get('exp-duration')
        h = 0
        for i in college:
            if i != "":
                education = Education(college=college[h], degree=degree[h], duration=col_dur[h], score=score[h])
                education.save()
                new_cv.education.add(education)
            h += 1
        h = 0
        for i in comp:
            if i != "":
                exp = Experience(company=comp[h], position=position[h], duration=exp_dur[h], work=work[h])
                exp.save()
                new_cv.experience.add(exp)
            h += 1
        return redirect('cvview',id = new_cv.pk)

    if not request.user.is_anonymous:
        context = {"user": request.user}
    return render(request, 'cvmake.html', context)

def cvview(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    cv = CV.objects.get(pk=id)
    return render(request, 'cvview.html',
           {'cv': cv, 'edu': cv.education.all(), 'exp': cv.experience.all()})

def cvprint(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    new_cv = CV.objects.get(pk=id)
    if new_cv.user.pk != request.user.pk:
        return redirect('cvmake')
    template = loader.get_template('cvprint.html')
    html = template.render({'cv': new_cv, 'edu': new_cv.education.all(), 'exp': new_cv.experience.all()})
    option = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        'enable-local-file-access': None
    }
    print(settings.STATICFILES_DIRS[0])
    css = '/home/shivansh/PycharmProjects/CV_Maker/cvm/static/css/cv.css'

    pdf = pdfkit.from_string(html, False, option,css=css)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachments;filename=resume.pdf;'
    return response


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {"form": form})

def reslist(request):
    cv  = request.user.cv.all().order_by('-created_at').values()
    context = {"cvs": cv}
    return render(request,'resumelist.html',context)

def delresume(request,id):
    if not request.user.is_authenticated:
        return redirect('login')
    cv = CV.objects.get(pk=id)
    if cv.user.pk != request.user.pk:
        return redirect('cvmake')
    cv.delete()
    return redirect('reslist')

def updateresume(request,id):

    if not request.user.is_authenticated:
        return redirect('login')
    _cv = CV.objects.filter(pk=id)
    new_cv = _cv.first()
    print(new_cv.user)
    if new_cv.user.pk != request.user.pk:
        return redirect('cvmake')

    if request.method == "POST":
        data = dict(request.POST)
        name = data.get('name')[0]
        email = data.get('email')[0]
        phone = data.get('phone')[0]
        skills = data.get('skills')[0]
        about = data.get('about')[0]
        interests = data.get('interests')[0]
        _cv.update(skills=skills, name=name, email=email, phone=phone, about=about, interests=interests)
        request.user.cv.add(new_cv)
        college = list(data.get('college'))
        degree = data.get('degree')
        score = data.get('score')
        col_dur = data.get('col-duration')
        comp = data.get('company')
        work = data.get('work')
        position = data.get('position')
        exp_dur = data.get('exp-duration')
        h = 0
        new_cv.education.clear()
        Education.objects.filter(cv=None).delete()
        new_cv.experience.clear()
        Experience.objects.filter(cv=None).delete()
        for i in college:
            if i != "":
                education = Education(college=college[h], degree=degree[h], duration=col_dur[h], score=score[h])
                education.save()
                new_cv.education.add(education)
            h += 1
        h = 0
        for i in comp:
            if i != "":
                exp = Experience(company=comp[h], position=position[h], duration=exp_dur[h], work=work[h])
                exp.save()
                new_cv.experience.add(exp)
            h += 1
        return redirect('cvview',id = new_cv.pk)
    if not request.user.is_anonymous:
        context = {"user": request.user,"cv":new_cv}
    return render(request, 'cvmake.html', context)




