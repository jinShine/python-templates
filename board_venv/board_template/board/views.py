from django.shortcuts import render, redirect
from django.http import Http404
from .models import Board
from register.models import User

def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시물을 찾을 수 없습니다.')

    return render(request, "board_detail.html", { 'board' : board })

def baord_write(request):

    if not (request.session.get('user')):
        return redirect('/user/signin')

    if request.method == "POST":

        user_id = request.session.get('user')
        writer = User.objects.get(pk=user_id)

        title = request.POST.get('title')
        content = request.POST.get('content')

        board = Board()
        board.title = title
        board.contents = content
        board.writer = writer

        board.save()

        return redirect('/board/list')
    else:
        return render(request, "board_write.html")

def baord_list(request):

    # 모든 게시글을 가져올껀데 -은 역순이라 가장 최신것을 가져오게된다.
    boards = Board.objects.all().order_by('-id')
    return render(request, "board_list.html", { 'boards' : boards })