from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import User

def register(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        user_name = request.POST.get("user-name", None)
        user_email = request.POST.get("user-email", None)
        user_password = request.POST.get("user-password", None)
        user_re_password = request.POST.get("user-re-password", None)
        user_age = request.POST.get("user-age", None)

        res_data = {}

        if not (user_name and user_email and user_password and user_re_password):
            res_data["error"] = "모든 값을 입력 해야됩니다."
        elif user_re_password != user_password:
            res_data["error"] = "비밀번호가 다릅니다."
        else:
            user = User(
                name = user_name,
                email = user_email,
                password = make_password(user_password),
                age = user_age
            )

            user.save()

        return render(request, 'signup.html', res_data)
