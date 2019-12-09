from django.db import models


class Customer(models.Model):
    FEMALE = 0
    MALE = 1
    SEX_CHOICES = (
        (MALE, '男'),
        (FEMALE, '女')
    )

    STATUS_NORMAL = 0
    STATUS_DENY = -1
    STATUS_CHOICES = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DENY, '已禁用')
    )
    account = models.CharField(max_length=15, verbose_name='账号')
    password = models.CharField(max_length=20, verbose_name='密码')
    name = models.CharField(max_length=6, verbose_name='姓名')
    sex = models.PositiveSmallIntegerField(choices=SEX_CHOICES, verbose_name='性别')
    student_id = models.CharField(max_length=9, null=True, verbose_name='学号')
    enter_year = models.PositiveIntegerField(verbose_name='入学年份')
    college_name = models.CharField(max_length=20, null=True, verbose_name="系名")
    class_name = models.CharField(max_length=20, null=True, verbose_name='专业班级')
    recommender = models.ForeignKey(to='self', null=True, verbose_name='推荐人')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)

    class Meta:
        verbose_name = '客户表'
        ordering = '-created_time'

    def __str__(self):
        return f'<customer-{self.name}>'
