from django.db import models


class ContestType(models.Model):
    title = models.CharField(max_length=20, verbose_name='试卷名')
    contest_id = models.SmallIntegerField(verbose_name='考试id')

    class Meta:
        verbose_name = '考试类型表'

    def __str__(self):
        return f'<contest_type-{self.title}>'
