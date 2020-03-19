from django.db import models

class User(models.Model):
    name = models.CharField(max_length=32,
                            null=False,
                            verbose_name="사용자명")
    password = models.CharField(max_length=8,
                                null=False,
                                verbose_name="비밀번호")
    age = models.CharField(max_length=3,
                           null=True,
                           verbose_name="나이")
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name="등록시간")

    def __str__(self):
        return self.username

    # 데이터 베이스 테이블명 지정 방법
    class Meta:
        db_table = "signup_user"
        verbose_name = "사용자"
        verbose_name_plural = "사용자"


