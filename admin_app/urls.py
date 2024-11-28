from django.urls import path
from .views import (home_page, login_page, logout_page, profile,
                    faculty_list, faculty_create, faculty_edit, faculty_delete,
                    kafedra_list, kafedra_create, kafedra_edit, kafedra_delete,
                    subject_list, subject_create, subject_edit, subject_delete,
                    teacher_list, teacher_create, teacher_edit, teacher_delete,
                    group_list, group_create, group_edit, group_delete,
                    student_list, student_create, student_edit, student_delete)

urlpatterns = [
    path('', home_page, name='home-page'),
    path('login/', login_page, name='login-page'),
    path('logout/', logout_page, name='logout-page'),

    path('faculty/list/', faculty_list, name="faculty-list"),
    path('faculty/create/', faculty_create, name="faculty-create"),
    path('faculty/<int:pk>/edit/', faculty_edit, name="faculty-edit"),
    path('faculty/<int:pk>/delete/', faculty_delete, name="faculty-delete"),

    path('kafedra/list/', kafedra_list, name="kafedra-list"),
    path('kafedra/create/', kafedra_create, name="kafedra-create"),
    path('kafedra/<int:pk>/edit/', kafedra_edit, name="kafedra-edit"),
    path('kafedra/<int:pk>/delete/', kafedra_delete, name="kafedra-delete"),

    path('subject/list/', subject_list, name="subject-list"),
    path('subject/create/', subject_create, name="subject-create"),
    path('subject/<int:pk>/edit/', subject_edit, name="subject-edit"),
    path('subject/<int:pk>/delete/', subject_delete, name="subject-delete"),

    path('teacher/list/', teacher_list, name="teacher-list"),
    path('teacher/create/', teacher_create, name="teacher-create"),
    path('teacher/<int:pk>/edit/', teacher_edit, name="teacher-edit"),
    path('teacher/<int:pk>/delete/', teacher_delete, name="teacher-delete"),

    path('group/list/', group_list, name="group-list"),
    path('group/create/', group_create, name="group-create"),
    path('group/<int:pk>/edit/', group_edit, name="group-edit"),
    path('group/<int:pk>/delete/', group_delete, name="group-delete"),

    path('student/list/', student_list, name="student-list"),
    path('student/create/', student_create, name="student-create"),
    path('student/<int:pk>/edit/', student_edit, name="student-edit"),
    path('student/<int:pk>/delete/', student_delete, name="student-delete"),
    path('profile/', profile, name="profile"),
]
