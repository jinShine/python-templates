from django.db import models

class User(models.Model):
    name = models.CharField(max_length=10,
                            null=False,
                            verbose_name='사용자명')
    password = models.CharField(max_length=8,
                                null=False,
                                verbose_name='비밀번호')
    email = models.EmailField(max_length=64,
                              null=False,
                              verbose_name='이메일')
    age = models.CharField(max_length=3,
                           null=False,
                           verbose_name='나이')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='등록시간')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'register_user'
        verbose_name_plural = '회원들'