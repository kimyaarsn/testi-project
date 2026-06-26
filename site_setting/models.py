from django.db import models

# Create your models here.

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name="نام سایت")
    site_url = models.CharField(max_length=200, verbose_name="دامنه سایت")
    address = models.TextField(max_length=200, verbose_name="آدرس")
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name="تلفن")
    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name="ایمیل")
    copy_right = models.CharField(max_length=300, null=True, blank=True, verbose_name="متن کپی رایت")
    about_us_text = models.TextField(max_length=200, verbose_name="متن درباره ما سایت")
    site_logo = models.ImageField(upload_to="site_setting/", verbose_name="لوگو سایت")
    video_background = models.FileField(upload_to='site/videos/',blank=True,null=True,verbose_name='ویدیوی پس زمینه')
    facebook_link = models.URLField(
        blank=True,
        null=True,
        verbose_name='لینک فیسبوک'
    )

    twitter_link = models.URLField(
        blank=True,
        null=True,
        verbose_name='لینک توییتر'
    )

    youtube_link = models.URLField(
        blank=True,
        null=True,
        verbose_name='لینک یوتیوب'
    )

    pinterest_link = models.URLField(
        blank=True,
        null=True,
        verbose_name='لینک پینترست'
    )

    tumblr_link = models.URLField(
        blank=True,
        null=True,
        verbose_name='لینک تامبلر'
    )

    rss_link = models.URLField(
        blank=True,
        null=True,
        verbose_name='لینک RSS'
    )

    instagram_link = models.URLField(
        blank=True,
        null=True,
        verbose_name='لینک اینستاگرام'
    )

    linkedin = models.URLField(
        blank=True,
        null=True,
        verbose_name='لینک لینکدین'
    )

    is_main_setting = models.BooleanField(verbose_name="تنظیمات اصلی")


    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name='تنظیمات سایت'
        verbose_name_plural='تنظیمات سایت'


class Banner(models.Model):
    title = models.CharField(
        max_length=300,
        verbose_name='عنوان بنر'
    )

    description = models.TextField(
        verbose_name='توضیحات بنر'
    )

    background = models.ImageField(
        upload_to='sliders/',
        verbose_name='بکگراند بنر'
    )

    image = models.ImageField(
        upload_to='sliders/',
        verbose_name='تصویر بنر'
    )


    is_active = models.BooleanField(
        default=True,
        verbose_name='فعال / غیرفعال'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بنر'
        verbose_name_plural = 'بنرهای سایت'

class CompanyLogo(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='نام شرکت'
    )

    image = models.ImageField(
        upload_to='partners/',
        verbose_name='لوگوی شرکت'
    )

    link = models.URLField(
        blank=True,
        null=True,
        verbose_name='لینک شرکت'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'لوگوی همکار'
        verbose_name_plural = 'لوگوهای همکاران'


class About(models.Model):
    title = models.CharField(max_length=200 ,  verbose_name='عنوان معرفی صفحه اصلی')
    text = models.TextField(verbose_name='متن معرفی')
    description = models.TextField(verbose_name='متن معرفی2')
    feature_1 = models.CharField(max_length=200,verbose_name='ویژگی اول')
    feature_2 = models.CharField(max_length=200,verbose_name='ویژگی دوم')
    feature_3 = models.CharField(max_length=200,verbose_name='ویژگی سوم')
    main_img = models.ImageField(upload_to='site/about/',verbose_name='تصویر معرفی اصلی')


    class Meta:
        verbose_name = 'تنظیمات سکشن معرفی '
        verbose_name_plural = ' تنظیمات سکشن معرفی'



class CallToAction(models.Model):
    become_instructor_title = models.CharField(max_length=300,verbose_name='عنوان بخش مربی')
    become_instructor_text = models.TextField(verbose_name='متن بخش مربی')
    student_title = models.CharField(max_length=300,verbose_name='عنوان بخش دانشجو')
    student_text = models.TextField(verbose_name='متن بخش دانشجو')

    class Meta:
        verbose_name = 'تنظیمات دعوت به همکاری '
        verbose_name_plural = ' تنظیمات دعوت به همکاری'


class  AbouUsFeature(models.Model):
    title = models.CharField(max_length=300 , verbose_name='عنوان صفحه درباره ما')
    text = models.TextField(verbose_name='توضیحات صفحه درباره ما')


    feature_1_title = models.CharField(max_length=200, verbose_name='عنوان ویژگی اول')
    feature_1_text = models.TextField(verbose_name='متن ویژگی اول')

    feature_2_title = models.CharField(max_length=200, verbose_name='عنوان ویژگی دوم')
    feature_2_text = models.TextField(verbose_name='متن ویژگی دوم')

    feature_3_title = models.CharField(max_length=200, verbose_name='عنوان ویژگی سوم')
    feature_3_text = models.TextField(verbose_name='متن ویژگی سوم')

    feature_4_title = models.CharField(max_length=200, verbose_name='عنوان ویژگی چهارم')
    feature_4_text = models.TextField(verbose_name='متن ویژگی چهارم')

    class Meta:
          verbose_name = 'تنظیمات ویژگی صفحه درباره ما '
          verbose_name_plural = 'تنظیمات ویژگی صفحه درباره ما'


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'عنوان لینک فوتر'
        verbose_name_plural = 'عنوان لینک های فوتر'


class FooterLink(models.Model):
    title = models.CharField(max_length=200 , verbose_name='عنوان')
    url = models.CharField(max_length=200 , verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox , on_delete=models.CASCADE,verbose_name='دسته بندی',related_name='links')

    class Meta:
        verbose_name='لینک فوتر'
        verbose_name_plural=' لینک های فوتر'

    def __str__(self):
        return self.title




