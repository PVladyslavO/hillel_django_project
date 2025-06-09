from django import forms
from api.models import Employee  # Make sure Employee is imported correctly
from common.enums import WorkDayEnum

class WorkDayForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), required=True)
    work_day_type = forms.ChoiceField(choices=[(e.value, e.name) for e in WorkDayEnum])
    date = forms.DateField()

    def clean_employee(self):
        employee = self.cleaned_data.get('employee')
        if not employee:
            raise forms.ValidationError("Employee must be selected.")
        return employee

    def clean(self):
        cleaned_data = super().clean()
        employee = cleaned_data.get('employee')
        work_day_type = cleaned_data.get('work_day_type')

        if not employee:
            return cleaned_data

        # Count sick days for this employee
        sick_days_count = self._get_days_count(employee, WorkDayEnum.SICK_DAY.value)
        if work_day_type == WorkDayEnum.SICK_DAY.value:
            sick_days_count += 1
        if sick_days_count > 5:
            raise forms.ValidationError("Кількість лікарняних днів не може перевищувати 5.")

        # Count holidays for this employee
        holiday_days_count = self._get_days_count(employee, WorkDayEnum.HOLIDAY.value)
        if work_day_type == WorkDayEnum.HOLIDAY.value:
            holiday_days_count += 1
        if holiday_days_count > 3:
            raise forms.ValidationError("Кількість днів відпочинку не може перевищувати 3.")

        return cleaned_data

    def _get_days_count(self, employee, day_type):
        # Replace this with your actual model for storing work days
        from api.models import WorkDay  # Assuming you have a WorkDay model
        return WorkDay.objects.filter(employee=employee, work_day_type=day_type).count()
