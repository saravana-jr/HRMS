from django import forms
from .models import LeaveRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Field
from crispy_forms.layout import Layout,Div


class LeaveRequestForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = LeaveRequest
        fields =  ('leave_type', 'start_date', 'end_date', 'description', 'No_of_Leaves')
        
    
    def __init__(self,*args,**kwargs) -> None:
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_method='POST'
        self.helper.add_input(Submit('submit','Submit', css_class="mt-7 text-white bg-blue-500 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"))
        self.helper.layout=Layout(Div(
            Field('leave_type',  css_class='form-input mt-4'),
            Field('start_date', css_class='form-input datepicker'),
            Field('end_date', css_class='form-input datepicker'),
            Field('description', css_class='form-input rounded-md border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 focus:ring-opacity-50'),
            Field('No_of_Leaves', css_class='form-input mt-4 mb-4'),
            css_class='grid grid-cols-1 gap-4 w-6/12'))
       
    