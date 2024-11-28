from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .services import (get_faculties, get_kafedras,
                       get_subjects, get_teachers,
                       get_groups, get_students)
from .forms import (FacultyModelForm, KafedraModelForm,
                    SubjectModelForm, TeacherModelForm,
                    GroupModelForm, StudentModelForm)
from .models import (Faculty, Kafedra,
                     Subject, Teacher,
                     Group, Student)


# Create your views here.
def login_required_decorator(func):
    return login_required(function=func, login_url='login-page')


def login_page(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)

        if user is not None:
            login(request=request, user=user)
            return redirect('home-page')

    return render(request, template_name='login.html')


@login_required_decorator
def logout_page(request):
    logout(request=request)

    return redirect('login-page')


@login_required_decorator
def home_page(request):
    faculties = get_faculties()
    kafedras = get_kafedras()
    subjects = get_subjects()
    teachers = get_teachers()
    groups = get_groups()
    students = get_students()
    context = {
        'counts':
            {
                'faculties': len(faculties),
                'kafedras': len(kafedras),
                'subjects': len(subjects),
                'teachers': len(teachers),
                'groups': len(groups),
                'students': len(students),
            }
    }
    return render(request=request, template_name='index.html', context=context)


@login_required_decorator
def faculty_list(request):
    faculties = get_faculties()
    context = {
        'faculties': faculties
    }
    return render(request=request, template_name="faculty/list.html", context=context)


@login_required_decorator
def faculty_create(request):
    model = Faculty()
    form = FacultyModelForm(data=request.POST, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created faculty: {request.POST.get('name')}"]
        request.session['actions'] = actions

        faculty_count = request.session.get('faculty_count', 0)
        faculty_count += 1
        request.session['faculty_count'] = faculty_count

        return redirect("faculty-list")

    context = {
        'form': form
    }
    return render(request=request, template_name="faculty/form.html", context=context)


@login_required_decorator
def faculty_edit(request, pk):
    model = Faculty.objects.get(pk=pk)
    form = FacultyModelForm(data=request.POST or None, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited faculty: {request.POST.get('name')}"]
        request.session['actions'] = actions

        return redirect('faculty-list')

    context = {
        'model': model,
        'form': form
    }
    return render(request=request, template_name="faculty/form.html", context=context)


@login_required_decorator
def faculty_delete(request, pk):
    model = Faculty.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted faculty: id={pk}"]
    request.session['actions'] = actions

    return redirect('faculty-list')


@login_required_decorator
def kafedra_list(request):
    kafedras = get_kafedras()
    context = {
        'kafedras': kafedras
    }
    return render(request=request, template_name='kafedra/list.html', context=context)


@login_required_decorator
def kafedra_create(request):
    model = Kafedra()
    form = KafedraModelForm(data=request.POST, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created kafedra: {request.POST.get('name')}"]
        request.session['actions'] = actions

        kafedra_count = request.session.get('kafedra_count', 0)
        kafedra_count += 1
        request.session['kafedra_count'] = kafedra_count

        return redirect("kafedra-list")

    context = {
        'form': form
    }
    return render(request=request, template_name="kafedra/form.html", context=context)


@login_required_decorator
def kafedra_edit(request, pk):
    model = Kafedra.objects.get(pk=pk)
    form = KafedraModelForm(data=request.POST or None, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited kafedra: {request.POST.get('name')}"]
        request.session['actions'] = actions

        return redirect('kafedra-list')

    context = {
        'model': model,
        'form': form
    }
    return render(request=request, template_name="kafedra/form.html", context=context)


@login_required_decorator
def kafedra_delete(request, pk):
    model = Kafedra.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted kafedra: id={pk}"]
    request.session['actions'] = actions

    return redirect('kafedra-list')


@login_required_decorator
def subject_list(request):
    subjects = get_subjects()
    context = {
        'subjects': subjects
    }
    return render(request=request, template_name='subject/list.html', context=context)


@login_required_decorator
def subject_create(request):
    model = Subject()
    form = SubjectModelForm(data=request.POST, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created subject: {request.POST.get('name')}"]
        request.session['actions'] = actions

        subject_count = request.session.get('subject_count', 0)
        subject_count += 1
        request.session['subject_count'] = subject_count

        return redirect("subject-list")

    context = {
        'form': form
    }
    return render(request=request, template_name="subject/form.html", context=context)


@login_required_decorator
def subject_edit(request, pk):
    model = Subject.objects.get(pk=pk)
    form = SubjectModelForm(data=request.POST or None, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited subject: {request.POST.get('name')}"]
        request.session['actions'] = actions

        return redirect('subject-list')

    context = {
        'model': model,
        'form': form
    }
    return render(request=request, template_name="subject/form.html", context=context)


@login_required_decorator
def subject_delete(request, pk):
    model = Subject.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted subject: id={pk}"]
    request.session['actions'] = actions

    return redirect('subject-list')


@login_required_decorator
def teacher_list(request):
    teachers = get_teachers()
    context = {
        'teachers': teachers
    }
    return render(request=request, template_name='teacher/list.html', context=context)


@login_required_decorator
def teacher_create(request):
    model = Teacher()
    form = TeacherModelForm(data=request.POST, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You added teacher: {request.POST.get('first_name')}"]
        request.session['actions'] = actions

        teacher_count = request.session.get('teacher_count', 0)
        teacher_count += 1
        request.session['teacher_count'] = teacher_count

        return redirect("teacher-list")

    context = {
        'form': form
    }
    return render(request=request, template_name="teacher/form.html", context=context)


@login_required_decorator
def teacher_edit(request, pk):
    model = Teacher.objects.get(pk=pk)
    form = TeacherModelForm(data=request.POST or None, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited teacher: {request.POST.get('first_name')}"]
        request.session['actions'] = actions

        return redirect('teacher-list')

    context = {
        'model': model,
        'form': form
    }
    return render(request=request, template_name="teacher/form.html", context=context)


@login_required_decorator
def teacher_delete(request, pk):
    model = Teacher.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted teacher: id={pk}"]
    request.session['actions'] = actions

    return redirect('teacher-list')


@login_required_decorator
def group_list(request):
    groups = get_groups()
    context = {
        'groups': groups
    }
    return render(request=request, template_name='group/list.html', context=context)


@login_required_decorator
def group_create(request):
    model = Group()
    form = GroupModelForm(data=request.POST, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created group: {request.POST.get('name')}"]
        request.session['actions'] = actions

        group_count = request.session.get('group_count', 0)
        group_count += 1
        request.session['group_count'] = group_count

        return redirect("group-list")

    context = {
        'form': form
    }
    return render(request=request, template_name="group/form.html", context=context)


@login_required_decorator
def group_edit(request, pk):
    model = Group.objects.get(pk=pk)
    form = GroupModelForm(data=request.POST or None, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited group: {request.POST.get('name')}"]
        request.session['actions'] = actions

        return redirect('group-list')

    context = {
        'model': model,
        'form': form
    }
    return render(request=request, template_name="group/form.html", context=context)


@login_required_decorator
def group_delete(request, pk):
    model = Group.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted group: id={pk}"]
    request.session['actions'] = actions

    return redirect('group-list')


@login_required_decorator
def student_list(request):
    students = get_students()
    context = {
        'students': students
    }
    return render(request=request, template_name='student/list.html', context=context)


@login_required_decorator
def student_create(request):
    model = Student()
    form = StudentModelForm(request.POST or None, request.FILES or None, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You created student: {request.POST.get('first_name')}"]
        request.session['actions'] = actions

        student_count = request.session.get('student_count', 0)
        student_count += 1
        request.session['student_count'] = student_count

        return redirect("student-list")

    context = {
        'form': form
    }
    return render(request=request, template_name="student/form.html", context=context)


@login_required_decorator
def student_edit(request, pk):
    model = Student.objects.get(pk=pk)
    form = StudentModelForm(request.POST or None, request.FILES or None, instance=model)

    if request.POST and form.is_valid():
        form.save()

        actions = request.session.get('actions', [])
        actions += [f"You edited student: {request.POST.get('first_name')}"]
        request.session['actions'] = actions

        return redirect('student-list')

    context = {
        'model': model,
        'form': form
    }
    return render(request=request, template_name="student/form.html", context=context)


@login_required_decorator
def student_delete(request, pk):
    model = Student.objects.get(pk=pk)
    model.delete()

    actions = request.session.get('actions', [])
    actions += [f"You deleted student: id={pk}"]
    request.session['actions'] = actions

    return redirect('student-list')


@login_required_decorator
def profile(request):
    return render(request=request, template_name='profile.html')
