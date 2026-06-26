from django import forms
from .models import CourseComment

class CourseCommentForm(forms.ModelForm):
    class Meta:
        model = CourseComment
        fields = ['name', 'email', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام شما'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'ایمیل شما'}),
            'text':forms.Textarea(attrs={'class':'form-control','placeholder':'متن نظر'})
        }
        labels = {
            'name': 'نام و نام خانوادگی',
            'email': 'آدرس پستی الکترونیکی',
            'text': ' اینجا پیام را تایپ کنید',
        }

    def clean(self):
        clean_data=super().clean()
        name=clean_data.get('name')
        email=clean_data.get('email')

        if not self.instance.user:
            if not name:
                raise forms.ValidationError('لطفا نام خود را وارد کنید')
            if not email:
               raise forms.ValidationError('لطفا ایمیل خود را وارد کنید')
        return clean_data