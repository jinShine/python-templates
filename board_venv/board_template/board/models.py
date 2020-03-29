from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='제목')
    # TextField는 길이에 제한이 없다.
    contents = models.TextField(verbose_name='내용')
    #to: 다른 DB와 연결 하겠다.
    #register app에 User모델과 연결하겠다.
    writer = models.ForeignKey('register.User',
                               null=True,
                               on_delete=models.CASCADE,
                               verbose_name='작성자')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           null=True,
                                           verbose_name='등록시간')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'board'
        verbose_name = '게시글'
        verbose_name_plural = '게시글'

