import pdfkit
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .forms import RegisterForm
from .models import CV
from .utils import save_resume


def create_resume(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        data = dict(request.POST)
        cv = save_resume(data, request.user, "save", None)
        return redirect('view-resume', id=cv.pk)

    if not request.user.is_anonymous:
        context = {"user": request.user}
    return render(request, 'create_resume.html', context)


def view_resume(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    cv = CV.objects.get(pk=id)
    return render(request, 'view_resume.html',
                  {'cv': cv, 'edu': cv.education.all(), 'exp': cv.experience.all()})


def update_resume(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    _cv = CV.objects.filter(pk=id)
    new_cv = _cv.first()
    if new_cv.user.pk != request.user.pk:
        return redirect('create-resume')

    if request.method == "POST":
        data = dict(request.POST)
        cv = save_resume(data, request.user, "update", _cv)
        return redirect('view-resume', id=cv.pk)
    if not request.user.is_anonymous:
        context = {"user": request.user, "cv": new_cv}
    return render(request, 'create_resume.html', context)


def print_resume(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    new_cv = CV.objects.get(pk=id)
    if new_cv.user.pk != request.user.pk:
        return redirect('create-resume')
    template = loader.get_template('print_resume.html')
    html = template.render({'cv': new_cv, 'edu': new_cv.education.all(), 'exp': new_cv.experience.all()})
    option = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        'enable-local-file-access': None
    }
    css = '/home/shivansh/PycharmProjects/CV_Maker/cvm/static/css/cv.css'
    pdf = pdfkit.from_string(html, False, option, css=css)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachments;filename=resume.pdf;'
    return response


def user_resume(request):
    cv = request.user.cv.all().order_by('-created_at').values()
    context = {"cvs": cv}
    return render(request, 'user_resume.html', context)


def delete_resume(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    cv = CV.objects.get(pk=id)
    if cv.user.pk != request.user.pk:
        return redirect('create-resume')
    cv.delete()
    return redirect('user-resume')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {"form": form})
