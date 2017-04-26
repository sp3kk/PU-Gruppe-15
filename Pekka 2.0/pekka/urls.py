from django.conf.urls import url
from . import views

app_name = 'pekka'

urlpatterns = [
    # login and register
    url(r'^$', views.login_user, name='login_user'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    # main views
    url(r'^ask/$', views.ask, name='ask'),
    url(r'^answer/$', views.answer, name='answer'),
    url(r'^about/$', views.about, name='about'),
    # question and voting
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<answer_id>[0-9]+)/vote_answer/$', views.vote_answer, name='vote_answer'),
    url(r'^(?P<question_id>[0-9]+)/vote_question/$', views.vote_question, name='vote_question'),
    # courses
    url(r'^TDT4140_answer/$', views.course_answer, {'sub_code': 'TDT4140'}, name='TDT4140_answer'),
    url(r'^TDT4110_answer/$', views.course_answer, {'sub_code': 'TDT4110'}, name='TDT4110_answer'),
    url(r'^TDT4145_answer/$', views.course_answer, {'sub_code': 'TDT4145'}, name='TDT4145_answer'),
    url(r'^TDT4180_answer/$', views.course_answer, {'sub_code': 'TDT4180'}, name='TDT4180_answer'),
    url(r'^TTM4100_answer/$', views.course_answer, {'sub_code': 'TTM4100'}, name='TTM4100_answer'),

    url(r'^TDT4140_question/$', views.course_question, {'sub_code': 'TDT4140'}, name='TDT4140_question'),
    url(r'^TDT4110_question/$', views.course_question, {'sub_code': 'TDT4110'}, name='TDT4110_question'),
    url(r'^TDT4145_question/$', views.course_question, {'sub_code': 'TDT4145'}, name='TDT4145_question'),
    url(r'^TDT4180_question/$', views.course_question, {'sub_code': 'TDT4180'}, name='TDT4180_question'),
    url(r'^TTM4100_question/$', views.course_question, {'sub_code': 'TTM4100'}, name='TTM4100_question'),

    url(r'^TDT4140_similar/$', views.course_similar, {'sub_code': 'TDT4140'}, name='TDT4140_similar'),
    url(r'^TDT4110_similar/$', views.course_similar, {'sub_code': 'TDT4110'}, name='TDT4110_similar'),
    url(r'^TDT4145_similar/$', views.course_similar, {'sub_code': 'TDT4145'}, name='TDT4145_similar'),
    url(r'^TDT4180_similar/$', views.course_similar, {'sub_code': 'TDT4180'}, name='TDT4180_similar'),
    url(r'^TTM4100_similar/$', views.course_similar, {'sub_code': 'TTM4100'}, name='TTM4100_similar')
]
