from django.shortcuts import render

def baord_list(request):
    return render(request, "board_list.html")
