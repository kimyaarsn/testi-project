from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
   email_active_code = models.CharField(
      max_length=20,
      unique=True,
      blank=True,
      null=True,
      verbose_name='کد فعال‌سازی ایمیل'
   )

   email_active_code_created_date = models.DateTimeField(
      null=True,
      blank=True,
      verbose_name='زمان ایجاد کد فعال‌سازی'
   )

   password_reset_code = models.CharField(
      max_length=20,
      unique=True,
      blank=True,
      null=True,
      verbose_name='کد بازیابی رمز عبور'
   )

   password_reset_code_created_date = models.DateTimeField(
      null=True,
      blank=True,
      verbose_name='زمان ایجاد کد بازیابی رمز عبور'
   )

   avatar = models.ImageField(upload_to='user_avatars/',
        verbose_name='تصویر کاربر',
       default='default/default-yser.jpeg')

   class Meta:
      verbose_name = 'کاربر'
      verbose_name_plural = 'کاربران'

   def __str__(self):
      if self.first_name and self.last_name:
         return self.get_full_name()

      return self.email

