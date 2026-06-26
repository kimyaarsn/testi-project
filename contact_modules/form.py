from django import forms
from .models import Contact

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields =['Fullname','Email','Title','Message']
        widgets = {
            'Fullname':forms.TextInput(attrs={'class':'form-control' , 'placeholder':'نام و نام خانوادگی'}),
            'Email':forms.EmailInput(attrs={'class':'form-control' , 'placeholder':'ایمیل شما'}),
            'Title':forms.TextInput(attrs = {'class':'form-control' , 'placeholder':'موضوع پیام شما'}),
            'Message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'پیام شما','rows':'6','id':'cf-message'})
        }
        labels = {
            'Fullname': 'نام و نام خانوادگی',
            'Email':'ایمیل',
            'Title':'موضوع',
            'Message':'پیام خود را بنویسید'
        }

        error_messages = {
            'Fullname':{
                'required':'لطفا نام و نام خانوادگی را وارد کنید'
            }
        }


