from django.db import models
from django.urls import reverse
from account_modules.models import User



class BlogCategory(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='عنوان دسته بندی'
    )

    url_title = models.CharField(
        max_length=200,
        unique=True,
        verbose_name='عنوان در URL'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='فعال / غیرفعال'
    )

    is_delete = models.BooleanField(
        default=False,
        verbose_name='حذف شده / نشده'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی بلاگ'
        verbose_name_plural = 'دسته بندی های بلاگ'



class BlogTag(models.Model):
    caption = models.CharField(
        max_length=200,
        verbose_name='عنوان تگ'
    )

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'تگ بلاگ'
        verbose_name_plural = 'تگ های بلاگ'


class BlogAuthor(models.Model):
    full_name = models.CharField(
        max_length=200,
        verbose_name='نام نویسنده'
    )

    image = models.ImageField(
        upload_to='blog_authors/',
        verbose_name='تصویر نویسنده'
    )

    biography = models.TextField(
        verbose_name='بیوگرافی'
    )


    is_active = models.BooleanField(
        default=True,
        verbose_name='فعال / غیرفعال'
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'نویسنده بلاگ'
        verbose_name_plural = 'نویسندگان بلاگ'


class Blog(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name='عنوان مقاله'
    )

    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.CASCADE,
        related_name='blogs',
        verbose_name='دسته بندی'
    )

    author = models.ForeignKey(
        BlogAuthor,
        on_delete=models.CASCADE,
        related_name='blogs',
        verbose_name='نویسنده'
    )

    tags = models.ManyToManyField(
        BlogTag,
        blank=True,
        related_name='blogs',
        verbose_name='تگ ها'
    )

    image = models.ImageField(
        upload_to='blogs/',
        verbose_name='تصویر مقاله'
    )

    short_description = models.CharField(
        max_length=500,
        verbose_name='توضیحات کوتاه'
    )

    text = models.TextField(
        verbose_name='متن مقاله'
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ انتشار'
    )

    url_title = models.CharField(
        max_length=300,
        unique=True,
        verbose_name='عنوان در URL'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='فعال / غیرفعال'
    )

    is_delete = models.BooleanField(
        default=False,
        verbose_name='حذف شده / نشده'
    )

    visit_count = models.PositiveIntegerField(
        default=0,
        verbose_name='تعداد بازدید'
    )

    def get_absolute_url(self):
        return reverse(
            'blog_detail',
            args=[self.url_title]
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class BlogComment(models.Model):
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='مقاله'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='کاربر'
    )

    title = models.CharField(max_length=300, verbose_name="عنوان پیام")


    name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='نام و نام خانوادگی'
    )

    email = models.EmailField(
        null=True,
        blank=True,
        verbose_name='ایمیل'
    )

    text = models.TextField(
        verbose_name='متن نظر'
    )

    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ ثبت'
    )

    def __str__(self):
        return self.name or str(self.user)

    class Meta:
        ordering = ['-create_date']
        verbose_name = 'نظر مقاله'
        verbose_name_plural = 'نظرات مقاله'