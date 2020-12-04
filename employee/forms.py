from django import forms
from .models import Employee, Project

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
    class DateForm(forms.Form):
        date = forms.DateTimeField(input_formats=['%d/%m/%Y'])
    # def __init__ (self, *args, **kwargs):
    #       brand = kwargs.pop("brand")
    #       super(EmployeeForm, self).__init__(*args, **kwargs)
    #       self.fields["eids"].widget = forms.widgets.CheckboxSelectMultiple()
    #       self.fields["eids"].help_text = ""
    # class EmpForm(forms.Form): 
    #     em = forms.ChoiceField(choices = )
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        def __init__ (self, *args, **kwargs):
          brand = kwargs.pop("brand")
          super(ProjectForm, self).__init__(*args, **kwargs)
          self.fields["eids"].widget = forms.widgets.CheckboxSelectMultiple()
          self.fields["eids"].help_text = ""
    class DateForm(forms.Form):
        date = forms.DateTimeField(input_formats=['%d/%m/%Y'])