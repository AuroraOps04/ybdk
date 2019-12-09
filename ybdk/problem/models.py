from django.db import models


class Problem(models.Model):
    index = models.PositiveIntegerField(verbose_name='序号')
    answer = models.CharField(max_length=5, verbose_name='答案')

    class Meta:
        verbose_name = '题目表'

    def __str__(self):
        return f'<problem-{self.index}>'
