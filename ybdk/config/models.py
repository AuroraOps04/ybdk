from django.db import models


class SideBar(models.Model):
    STATUS_SHOW = 0
    STATUS_HIDDEN = 1
    STATUS_CHOICES = (
        (STATUS_SHOW, '显示'),
        (STATUS_HIDDEN, '隐藏'),
    )

    title = models.CharField(max_length=20, verbose_name='标题')
    content = models.CharField(max_length=500, verbose_name='内容')
    status = models.SmallIntegerField(choices=STATUS_CHOICES, verbose_name='状态')

    class Meta:
        verbose_name = '侧边栏'

    def __str__(self):
        return f'<sidebar-{self.title}>'
