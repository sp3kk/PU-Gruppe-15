from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, Http404, request
from django.shortcuts import render, get_object_or_404, redirect, render_to_response, reverse
from django.db.models import Q
from . forms import *
from .models import *
import datetime
from django.template import RequestContext, loader
from difflib import SequenceMatcher
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        answers = question.answer_set.all()
        score = question.get_score()

        form = AnswerForm(request.POST)

        if request.method == 'POST':

            if form.is_valid():
                answer = Answer()
                answer.answer_text=form.data['answer_text']
                answer.author = request.user
                answer.answer_time = datetime.datetime.now()
                answer.question = question
                answer.save()
                form = AnswerForm()
                return render(request, 'music/detail.html', {'score': score,
                                                             'question_title': question.question_title,
                                                             'question_content': question.question_content,
                                                             'sub_code': question.sub_code,
                                                             'answers': answers, 'form': form,
                                                             })

    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'music/detail.html', {'score': score,
                                                 'question_title': question.question_title,
                                                 'question_content': question.question_content,
                                                 'sub_code': question.sub_code,
                                                 'answers': answers, 'form': form})


def addQuestion(request):
    form = QuestionForm()
    if request.POST:
        form = QuestionForm(request.POST)
        if form.is_valid():
            author = form.save()
            question_title = QuestionForm.question_title.save()
            question_content = QuestionForm.question_content.save()
            return redirect('/index/')

    return render_to_response('Fagsider/questions.html', {'form': form}, context_type=RequestContext(request))


def vote_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    form = QuestionVotesForm()
    previous_page = request.META['HTTP_REFERER']
    if request.method == 'POST':
        form = QuestionVotesForm(request.POST)
        if form.is_valid():
            qv = QuestionVotes()
            qv.user = request.user
            qv.question = question
            qv.val = form.data['val']
            if not QuestionVotes.objects.filter(question=qv.question, user=qv.user):
                qv.save()
            else:
                existing_votes = QuestionVotes.objects.filter(question=question, user=qv.user)
                for vote in existing_votes:
                    vote.delete()
                qv.save()
            return HttpResponseRedirect('/' + question_id)
    return render(request, template_name='music/vote_question.html', context={
            'question_id': question_id,
            'question_title': question.question_title,
            'question_content': question.question_content,
            'score': question.get_score(),
            'form': form,
            'previous_page': previous_page,
    })


def vote_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    form = AnswerVotesForm()
    currentScore = answer.get_score()
    if request.method == 'POST':
        form = AnswerVotesForm(request.POST)
        if form.is_valid():
            answ = AnswerVotes()
            answ.user = request.user
            answ.ans = answer
            answ.val = form.data['val']
            if not AnswerVotes.objects.filter(ans=answer, user=answ.user):
                answ.save()
            else:
                existing_votes = AnswerVotes.objects.filter(ans=answer, user=answ.user)
                for vote in existing_votes:
                    vote.delete()
                answ.save()
            return HttpResponseRedirect('/' + str(answer.question.id))
    return render(request, template_name='music/vote_answer.html', context=
                  {'question': answer.question,
                   'answer': answer,
                   'score': currentScore,
                   'form': form,
                   })

#-------------------------------------------------------------------------------------------------------------------------------------

#Her kommer bot. Retur likehet vill bli tidligere spørsmål med svar når det er klart

def similar(a, b):
    likhet = SequenceMatcher(None, a, b).ratio()
    if likhet >= 0.5:
        likhet = request.session.get(b)
        return likhet
    else:
        return "ikke noe"

#-------------------------------------------------------------------------------------------------------------------------------------

def TDT4140_a(request):
    return render(request, 'Fagsider/TDT4140_a.html')

def TDT4110_a(request):
    return render(request, 'Fagsider/TDT4110_a.html')

def TDT4145_a(request):
    return render(request, 'Fagsider/TDT4145_a.html')

def TDT4180_a(request):
    return render(request, 'Fagsider/TDT4180_a.html')


def TTM4100_a(request):
    sub_code = 'TTM4100'
    # connecter til databasen
    all_questions_with_sub_code = Question.objects.filter(sub_code = sub_code)
    context = {
        'all_questions_with_sub_code': all_questions_with_sub_code,
    }
    return render(request, 'Fagsider/TTM4100_a.html', context=context)

def TTM4100_b(request):
    global c
    sub_code = 'TTM4100'
    all_questions_with_sub_code = Question.objects.filter(sub_code=sub_code)
    similar_questions = []

    a = Question.objects.filter(sub_code=sub_code).latest('ask_time')
    a_content = a.question_content

    for questions in all_questions_with_sub_code:
        b = questions.question_content

        likhet = SequenceMatcher(None, a_content, b).ratio()
        if likhet >= 0.5:
            similar_questions.append(questions)

    context = {
        'similar_questions': similar_questions
    }

    return render(request, 'Fagsider/TTM4100_b.html', context)


def TDT4140_q(request):
    sub_code = 'TDT4140'
    form_class = QuestionForm
    return render(request, 'Fagsider/TDT4140_q.html',{
    'form':form_class})

def TDT4110_q(request):
    sub_code = 'TDT4110'
    form_class = QuestionForm
    return render(request, 'Fagsider/TDT4110_q.html',{
    'form':form_class})

def TDT4145_q(request):
    sub_code = 'TDT4145'
    form_class = QuestionForm
    return render(request, 'Fagsider/TDT4145_q.html',{
    'form':form_class})

def TDT4180_q(request):
    sub_code = 'TDT4180'
    form_class = QuestionForm
    return render(request, 'Fagsider/TDT4180_q.html',{
    'form':form_class})

def TTM4100_q(request):
    sub_code = 'TTM4100'
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            question = Question()
            question.question_title = form.data['question_title']
            question.question_content = form.data['question_content']
            question.sub_code = sub_code
            question.author = request.user
            question.ask_time = datetime.datetime.now()
            question.save()
            return redirect("../../music/TTM4100_b")
        """""
        question.question_title= form.question_title.save_form_data()
        question.question_content = form.question_content
        return redirect('/music/')
        """""
    return render(request, 'Fagsider/TTM4100_q.html', {'form': form})



def create_album(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        form = AlbumForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.album_logo = request.FILES['album_logo']
            file_type = album.album_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'album': album,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'music/create_album.html', context)
            album.save()
            return render(request, 'music/detail.html', {'album': album})
        context = {
            "form": form,
        }
        return render(request, 'music/create_album.html', context)


def create_song(request, album_id):
    form = SongForm(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album, pk=album_id)
    if form.is_valid():
        albums_songs = album.song_set.all()
        for s in albums_songs:
            if s.song_title == form.cleaned_data.get("song_title"):
                context = {
                    'album': album,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'music/create_song.html', context)
        song = form.save(commit=False)
        song.album = album
        song.audio_file = request.FILES['audio_file']
        file_type = song.audio_file.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in AUDIO_FILE_TYPES:
            context = {
                'album': album,
                'form': form,
                'error_message': 'Audio file must be WAV, MP3, or OGG',
            }
            return render(request, 'music/create_song.html', context)

        song.save()
        return render(request, 'music/detail.html', {'album': album})
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'music/create_song.html', context)


def delete_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    album.delete()
    albums = Album.objects.filter(user=request.user)
    return render(request, 'music/index.html', {'albums': albums})


def delete_song(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request, 'music/detail.html', {'album': album})



def favorite(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    try:
        if song.is_favorite:
            song.is_favorite = False
        else:
            song.is_favorite = True
        song.save()
    except (KeyError, Song.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def favorite_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        if album.is_favorite:
            album.is_favorite = False
        else:
            album.is_favorite = True
        album.save()
    except (KeyError, Album.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        albums = Album.objects.filter(user=request.user)
        song_results = Song.objects.all()
        query = request.GET.get("q")
        if query:
            albums = albums.filter(
                Q(album_title__icontains=query) |
                Q(artist__icontains=query)
            ).distinct()
            song_results = song_results.filter(
                Q(song_title__icontains=query)
            ).distinct()
            return render(request, 'music/index.html', {
                'albums': albums,
                'songs': song_results,
            })
        else:
            return render(request, 'music/index.html', {'albums': albums})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
    context = {
        "form": form,
    }
    return render(request, 'music/register.html', context)


def songs(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        try:
            song_ids = []
            for album in Album.objects.filter(user=request.user):
                for song in album.song_set.all():
                    song_ids.append(song.pk)
            users_songs = Song.objects.filter(pk__in=song_ids)
            if filter_by == 'favorites':
                users_songs = users_songs.filter(is_favorite=True)
        except Album.DoesNotExist:
            users_songs = []
        return render(request, 'music/songs.html', {
            'song_list': users_songs,
            'filter_by': filter_by,
        })