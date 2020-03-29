from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='태그명')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           null=True,
                                           verbose_name='등록시간')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tag'
        verbose_name = '태그'
        verbose_name_plural = '태그'
