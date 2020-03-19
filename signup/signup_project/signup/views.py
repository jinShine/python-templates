from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import User

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        user_name = request.POST.get("user-name", None)
        password = request.POST.get("password", None)
        re_password = request.POST.get("re-password", None)
        user_age = request.POST.get("user-age", None)

        res_data = {}
        if not (user_name and password and re_password):
            res_data["error"] = "모든 값을 입력해야 합니다."
        elif password != re_password:
            res_data["error"] = "비밀번호가 다릅니다."
        else:
            print(user_name)
            print(password)
            user = User(
                name = user_name,
                password = make_password(password),
                age = user_age
            )

            user.save()
        return render(request, 'register.html', res_data)