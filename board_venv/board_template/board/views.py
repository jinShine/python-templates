from django.shortcuts import render, redirect
from .models import Board

def board_detail(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, "board_detail.html", { 'board' : board })

def baord_write(request):
    if request.method == "POST":

        title = request.POST.get('title')
        content = request.POST.get('content')

        board = Board()
        board.title = title
        board.contents = content

        board.save()

        return redirect('/board/list')
    else:
        return render(request, "board_write.html")

def baord_list(request):

    # 모든 게시글을 가져올껀데 -은 역순이라 가장 최신것을 가져오게된다.
    boards = Board.objects.all().order_by('-id')
    return render(request, "board_list.html", { 'boards' : boards })