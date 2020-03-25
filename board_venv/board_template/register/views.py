from django.shortcuts import render
from .models import User

def register(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        user_name = request.POST.get("user-name")
        user_email = request.POST.get("user-email")
        user_password = request.POST.get("user-password")
        user_re_password = request.POST.get("user-re-password")
        user_age = request.POST.get("user-age")

        res_data = {}

        if not (user_name and user_email and user_password and user_re_password and user_age):
            res_data["error"] = "모든 값을 입력 해줘야 합니다."
        elif user_password != user_re_password:
            res_data["error"] = "비밀번호가 다릅니다."
        else:
            userModel = User(
                name = user_name,
                email = user_email,
                password= user_re_password,
                age = user_age
            )

            userModel.save()

        return render(request, 'signup.html', res_data)
