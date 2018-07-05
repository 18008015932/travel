from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class City(models.Model): # 城市表
    cityid = models.IntegerField(primary_key=True)
    cityname = models.CharField(max_length=100)

    class Meta:
        db_table = 'city'
        verbose_name_plural = verbose_name = '城市'

    def __str__(self):
        return self.cityname



class Tag(models.Model): # 分类表
    tagid = models.IntegerField(primary_key=True)
    tagname = models.CharField(max_length=70)

    class Meta:
        db_table = 'tag'
        verbose_name_plural = verbose_name = '分类'

    def __str__(self):
        return self.tagname



class User(models.Model): # 用户表
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)  # 用户名
    tel = models.CharField(max_length=64)  # 用户电话
    email = models.EmailField('邮箱')  # 邮箱
    password = models.CharField(max_length=100)  # 密码
    icon = models.CharField(max_length=255)  # 头像

    class Meta:
        db_table = 'user'
        verbose_name_plural = verbose_name = '用户'

    def __str__(self):
        return self.username


class Article(models.Model): # 文章表
    articleid = models.AutoField(primary_key=True)
    # 作者，关联用户，当用户被删除，文章不做任何处理
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,verbose_name='作者')
    title = models.TextField('标题',max_length=100)   # 文章标题
    content = models.TextField('内容')  # 文章内容
    pub_time = models.DateField('日期',auto_now=True)  # 发布日期
    status = models.IntegerField(default=0)
    # city关联的是城市表
    city = models.ForeignKey(City,on_delete=models.SET_DEFAULT,default=1,verbose_name='城市')
    # 一篇文章对应多个分类，一个分类也对应多篇文章，多对多关系
    tag = models.ManyToManyField(Tag,verbose_name='分类')

    class Meta:
        db_table = 'article'
        verbose_name_plural = verbose_name = '文章'

    def __str__(self):
        return self.title


class Comment(models.Model): # 评论表
    com_id = models.AutoField(primary_key=True)
    com_content = models.TextField('评论内容')
    com_publish = models.DateField('时间',auto_now=True)
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name='文章')
    reply = models.ForeignKey('self',on_delete=models.DO_NOTHING,null=True,blank=True,verbose_name='回复')

    class Meta:
        db_table = 'comment'
        verbose_name_plural = verbose_name = '评论'

    def __str__(self):
        return self.com_content
