from .models import CV, Education, Experience


def save_resume(data, user, op, _cv):
    if op == "save":
        new_cv = CV(skills=data.get('skills')[0], name=data.get('name')[0], email=data.get('email')[0],
                    phone=data.get('phone')[0], about=data.get('about')[0], interests=data.get('interests')[0])

    else:
        _cv.update(skills=data.get('skills')[0], name=data.get('name')[0], email=data.get('email')[0],
                   phone=data.get('phone')[0], about=data.get('about')[0], interests=data.get('interests')[0])
        new_cv = _cv.first()
        new_cv.education.clear()
        Education.objects.filter(cv=None).delete()
        new_cv.experience.clear()
        Experience.objects.filter(cv=None).delete()

    new_cv.save()
    user.cv.add(new_cv)
    h = 0
    college = data.get('college')
    if college:
        for i in college:
            if i != "":
                education = Education(college=college[h], degree=data.get('degree')[h],
                                      duration=data.get('col-duration')[h], score=data.get('score')[h])
                education.save()
                new_cv.education.add(education)
            h += 1
        h = 0
    comp = data.get('company')
    if comp:
        for i in comp:
            if i != "":
                exp = Experience(company=comp[h], position=data.get('position')[h],
                                 duration=data.get('exp-duration')[h], work=data.get('work')[h])
                exp.save()
                new_cv.experience.add(exp)
            h += 1
    return new_cv


def find_cv(id):
    try:
        cv = CV.objects.get(pk=id)
    except CV.DoesNotExist:
        cv = None
    return cv
