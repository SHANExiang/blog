from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Classification(models.Model):
    aritcle_type = models.CharField(max_length=128, unique=True,
                                    verbose_name='文章类型', default='其它')
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(
        auto_now=True, verbose_name='更新日期')

    def __str__(self):
        return '<%s>' % self.aritcle_type

    class META:
        verbose_name = '文章分类'
        verbose_name_plural = "文章分类"
        ordering = ['-create_time']


class Article(models.Model):
    '''所有文章列表'''
    title = models.CharField(max_length=64, unique=True, verbose_name='标题')
    text = RichTextUploadingField(null=True, blank=True,
                            verbose_name='文章内容')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='标签')
    classification = models.ForeignKey(
        'Classification', null=True, blank=True, on_delete=models.SET_NULL,
        verbose_name='分类')
    comments = models.TextField(verbose_name='评论')
    likes = models.IntegerField(verbose_name='点赞数', default=0)
    notlikes = models.IntegerField(verbose_name='反对数', default=0)
    reads = models.IntegerField(verbose_name='阅读量', default=0)
    collections = models.IntegerField(verbose_name='收藏量', default=0)
    create_time = models.DateTimeField(
        auto_now_add=True, verbose_name='创建日期')
    update_time = models.DateTimeField(
        auto_now=True, verbose_name='更新日期')

    def __str__(self):
        return '<%s>--%s' % (self.title, self.classification)

    class META:
        verbose_name = '文章列表'
        verbose_name_plural = "文章列表"
        ordering = ['-create_time']


class Tag(models.Model):
    """标签"""
    name = models.CharField('标签名', max_length=32, unique=True)
    c_day = models.DateField('创建日期', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = "标签"




