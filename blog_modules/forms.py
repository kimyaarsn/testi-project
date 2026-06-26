from django import forms
from .models import BlogComment

class BlogCommentForm(forms.ModelForm):
    class Meta:
       model=BlogComment
       fields=['name', 'email', 'title', 'text']
       widgets={
           'name':forms.TextInput(attrs={
            'class':'form-control','placeholder':'نام '
            }),
           'email':forms.EmailInput(attrs={
            'class':'form-control', 'placeholder':'ایمیل '
            }),
           'title': forms.TextInput(attrs={
               'class': 'form-control', 'placeholder':' موضوع'
           }),

           'text': forms.Textarea(attrs={
               'class': 'form-control',
               'placeholder': 'پیام شما',
               'rows': '6',
               'id': 'cf-message'

           })

       }
       labels={
           'name':'نام و نام خانوادگی',
           'email':'ایمیل',
           'title':'موضوع',
           'text':'پیام خود را بنویسید'


       }
       error_messages={
           'name':{
               'required':'لطفا نام و نام خانوادگی را وارد کنید'

           }
       }