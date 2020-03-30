from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User


def signout(request):
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
                name=user_name,
                email=user_email,
                password=make_password(user_re_password),
                age=user_age
            )

            userModel.save()

        return render(request, 'signup.html', res_data)


def signin(request):
    if request.method == "GET":
        if request.session.get('user'):
            return redirect('/')
        else:
            return render(request, 'signin.html')
    elif request.method == "POST":
        user_name = request.POST.get("user-name", None)
        user_password = request.POST.get("user-password", None)

        res_data = {}

        if not (user_name and user_password):
            res_data["error"] = "모든 값을 입력 해야됩니다."
        else:
            try:
                user = User.objects.get(name=user_name)
            except User.DoesNotExist:
                res_data['error'] = "ID가 존재하지 않습니다."
                return

            if check_password(user_password, user.password):

                # 세션에 방금 로그인한 user의 id를 "user"키로 저장한다.
                request.session["user"] = user.id
                return redirect("/")

                # 성공, 로그인 처리
                # 세션 처리
                # home으로 리다이렉트
            else:
                res_data["error"] = "비밀번호를 틀렸습니다."

        return render(request, 'signin.html', res_data)


def logout(request):
    if request.session.get('user'):
        del (request.session['user'])

    return redirect('/')


def home(request):
    # template에서 로직 처리를 할 수 있다.
    return render(request, 'home.html')
