from django.db import models


class Submission(models.Model):
    STATUS_COMMITTED = 0
    STATUS_SUCCESS = 1
    STATUS_CHOICES = (
        (STATUS_COMMITTED, '已提交'),
        (STATUS_SUCCESS, '已完成')
    )

    contest_type = models.ForeignKey(to='ContentType', verbose_name='考试类型')
    score = models.SmallIntegerField(default=100, verbose_name='预期分数')
    user = models.ForeignKey(to='Customer', verbose_name='提交人')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    status = models.SmallIntegerField(choices=STATUS_CHOICES, verbose_name='状态')

    class Meta:
        verbose_name = '提交表'

    def __str__(self):
        return f'<submission-{self.user}-{self.contest_type}-{self.score}-{self.get_status_display()}'


class Result(models.Model):
    submission = models.ForeignKey(to='Submission', verbose_name='提交')
    score = models.SmallIntegerField(verbose_name='实际分数')
    success_time = models.DateTimeField(auto_now_add=True, verbose_name='完成时间')

    class Meta:
        verbose_name = '考试结果表'


