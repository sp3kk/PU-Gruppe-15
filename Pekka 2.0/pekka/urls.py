from django.conf.urls import url
from . import views


app_name = 'pekka'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.login_user, name='login_user'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    url(r'^ask/$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^answer/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    url(r'^about/$', views.create_album, name='create_album'),
    # url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),

    url(r'^TDT4140_a/$', views.TDT4140_a),
    url(r'^TDT4110_a/$', views.TDT4110_a),
    url(r'^TDT4145_a/$', views.TDT4145_a),
    url(r'^TDT4180_a/$', views.TDT4180_a),
    url(r'^TTM4100_a/$', views.TTM4100_a),

    url(r'^TDT4140_q/$', views.TDT4140_q),
    url(r'^TDT4110_q/$', views.TDT4110_q),
    url(r'^TDT4145_q/$', views.TDT4145_q),
    url(r'^TDT4180_q/$', views.TDT4180_q),
    url(r'^TTM4100_q/$', views.TTM4100_q),

    url(r'^TTM4100_b/$', views.TTM4100_b),

    url(r'^vote_answer/$', views.vote_answer, name='vote_answer'),
    url(r'^(?P<answer_id>[0-9]+)/vote_answer/$', views.vote_answer, name='vote_answer'),

    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^vote_question/$', views.vote_question, name='vote_question'),
    url(r'^(?P<question_id>[0-9]+)/vote_question/$', views.vote_question, name='vote_question'),

]
