from django.db import models
from django.urls import reverse
from account_modules.models import User


# Create your models here.

class CourseCategory(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='parentcategories')
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان دسته بندی')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف/حذف نشده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class CourseTag(models.Model):
    caption = models.CharField(max_length=300, verbose_name='عنوان تگ')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'




class Instructor(models.Model):
    full_name = models.CharField(max_length=150,verbose_name='نام و نام خانوادگی')
    title = models.CharField(max_length=100,default='معلم',verbose_name='سمت')
    avatar = models.ImageField(upload_to='instructors/',verbose_name='تصویر مدرس')
    bio = models.TextField(verbose_name='بیوگرافی')
    phone = models.CharField(max_length=20 , verbose_name='موبایل')
    email= models.EmailField(verbose_name = 'ایمیل')
    site_address=models.CharField(max_length=300,verbose_name='آدرس سایت')
    skype_address = models.CharField(max_length=300,verbose_name='آدرس skype')
    pintrest=models.URLField(blank=True,null=True,verbose_name='پینترست')
    instagram = models.URLField(blank=True,null=True,verbose_name='اینستاگرام')
    twitter = models.URLField(blank=True,null=True,verbose_name='توییتر')
    facebook = models.URLField(blank=True,null=True,verbose_name='فیسبوک')
    is_active = models.BooleanField(default=True,verbose_name='فعال')
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse(
            'instructor_detail',
            args=[self.id]
        )

    class Meta:
        verbose_name = 'مدرس'
        verbose_name_plural = 'مدرسان'

    def __str__(self):
        return self.full_name


class Course(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name="عنوان دوره")
    category = models.ForeignKey(CourseCategory, db_index=True, on_delete=models.CASCADE, null=True,
                                 related_name='courses', verbose_name='دسته بندی محصول')
    instructor = models.ForeignKey(Instructor,on_delete=models.CASCADE,related_name='courses',verbose_name='مدرس')
    course_tag = models.ManyToManyField(CourseTag, verbose_name='تگ محصول')
    price = models.IntegerField(default=0, verbose_name='قیمت')
    duration_days = models.PositiveIntegerField(verbose_name= 'مدت دوره')
    capacity= models.PositiveIntegerField(verbose_name='ظرفیت')
    short_description = models.CharField(max_length=400, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(null=True, verbose_name="توضیحات تکمیلی محصول")
    created_date= models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    image = models.ImageField(upload_to='courses/', default='courses/default.jpg', verbose_name='تصویر')
    url_title = models.CharField(max_length=300, default='', null=True, blank=True, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده / نشده')
    suggested_courses = models.ManyToManyField('self',blank=True,symmetrical=False, verbose_name="دوره های پیشنهادی")
    overview = models.TextField(verbose_name='بررسی اجمالی')
    section = models.TextField(verbose_name='برنامه تحصیلی')
    lecture_count = models.PositiveIntegerField(verbose_name='کل سخترانی ها')
    students_count = models.PositiveIntegerField(default=0, verbose_name=' تعداد دانشجوبان')
    has_certificate = models.BooleanField(default=0, verbose_name='دارای گواهینامه')

    def get_absolute_url(self):
        return reverse('course_detail', args=[self.url_title])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره ها'


class CourseComment(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='comments',verbose_name='دوره')
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,verbose_name='کاربر')
    create_date=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ثبت')
    text=models.TextField(verbose_name='متن نظر')
    name=models.CharField(max_length=100,null=True,blank=True,verbose_name='نام و نام خانوادگی')
    email=models.EmailField(null=True,blank=True,verbose_name='ایمیل')

    def __str__(self):
        return self.user.username if self.user else self.name

    class Meta:
        verbose_name ='نظر دوره'
        verbose_name_plural='نظرات دوره'






