from django import forms

class UploadPaymentForm(forms.Form):
    file = forms.FileField(label='Чек или платёжное поручение', help_text='PDF, JPG, PNG или TXT, до 10 МБ.')

    def clean_file(self):
        file = self.cleaned_data['file']
        if file.size > 10 * 1024 * 1024:
            raise forms.ValidationError('Максимальный размер файла — 10 МБ.')
        if file.name.rsplit('.', 1)[-1].lower() not in ['pdf', 'jpg', 'jpeg', 'png', 'txt']:
            raise forms.ValidationError('Выберите PDF, JPG, PNG или TXT.')
        return file
