from django.db import models
#
class User(models.Model):
    name = models.CharField(max_length=10,
                                null=False,
                                verbose_name="사용자명")
    password = models.CharField(max_length=8,
                                null=False,
                                verbose_name="비밀번호")
    email = models.EmailField(max_length=64,
                              null=False,
                              verbose_name="이메일")
    age = models.CharField(max_length=3,
                           null=True,
                           verbose_name="나이")
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')

    # 클래스가 문자열로 변환했을때 어떻게 변환할지 내장함수가 존재.
    # 문자열로 변환할때 호출하는 __str__
    def __str__(self):
        return self.name

    # 데이터 베이스에 테이블명 지정 방법
    class Meta:
        db_table = "signup_user"
        # verbose_name = "FC 사용자"
        verbose_name_plural = "회원들"  # 원래는 복수형(s)으로 나오게 되어있는데, 복수형 말고 수정하고싶을때!

