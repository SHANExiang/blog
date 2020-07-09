from django.db import models

# Create your models here.


class User(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    user_name = models.CharField(max_length=12, unique=True, verbose_name='姓名')
    password = models.CharField(max_length=56, verbose_name='密码')
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ['-create_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'




