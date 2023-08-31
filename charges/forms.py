from django import forms


class UploadPaymentForm(forms.Form):
    file = forms.FileField(label='')

    def createPayment():
        print('Form!')
        pass
