from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=128,
                             verbose_name='제목')
    # TextField는 길이에 제한이 없다.
    contents = models.TextField(verbose_name='내용')
    #to: 다른 DB와 연결 하겠다.
    # writer = models.ForeignKey()
