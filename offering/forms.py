from django import forms
from offering.models import Offering


class OfferingForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'type':'text',
        'class':'form-control',
        'id':'nome',
        'name':'nome'
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type':'email',
        'class':'form-control',
        'id':'email',
        'name':'email'
    }))

    offering_value = forms.DecimalField(min_value=0, decimal_places=2, widget=forms.TextInput(attrs={
        'type':'number',
        'class':'form-control',
        'id':'valor', 
        'name':'valor',
        'step': '.01',
        'min': '0'
    }))

    dedication = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'id':'observacoes',
        'name':'dedicacao',
        'rows':'3',
        'placeholder':'Nome da pessoa ou sua intenção ao oferecer'
    }))

    deposit_date = forms.CharField(widget=forms.TextInput(attrs={
        'type':'date',
        'class':'form-control',
        'id':'data',
        'name':'data'
    }))

    deposit_value = forms.DecimalField(min_value=0, decimal_places=2, widget=forms.TextInput(attrs={
        'type':'number',
        'class':'form-control',
        'id':'valor', 
        'name':'valor',
        'step': '.05',
        'min': '0'
    }))

    deposit_receipt = forms.FileField(widget=forms.FileInput(attrs={
        'type': 'file',
        'class': 'form-control-file',
        'name': 'comprovante',
        'id': 'comprovante'
    }))

    # ---------------------------------------------
    # Offerings types

    crescent_moon_tara_tsog = forms.DecimalField(required=False, min_value=0, decimal_places=2, widget=forms.TextInput(attrs={
        'type':'number',
        'class':'form-control',
        'id':'crescent_moon_tara_tsog', 
        'name':'crescent_moon_tara_tsog',
        'step': '.05',
        'min': '0'
    }))

    guru_tsog = forms.DecimalField(required=False, min_value=0, decimal_places=2, widget=forms.TextInput(attrs={
        'type':'number',
        'class':'form-control',
        'id':'guru_tsog', 
        'name':'guru_tsog',
        'step': '.05',
        'min': '0'
    }))

    waning_moon_tara_tsog = forms.DecimalField(required=False, min_value=0, decimal_places=2, widget=forms.TextInput(attrs={
        'type':'number',
        'class':'form-control',
        'id':'waning_moon_tara_tsog', 
        'name':'waning_moon_tara_tsog',
        'step': '.05',
        'min': '0'
    }))

    dakini_tsog = forms.DecimalField(required=False, min_value=0, decimal_places=2, widget=forms.TextInput(attrs={
        'type':'number',
        'class':'form-control',
        'id':'dakini_tsog', 
        'name':'dakini_tsog',
        'step': '.05',
        'min': '0'
    }))

    riwo_sangcho = forms.DecimalField(required=False, min_value=0, decimal_places=2, widget=forms.TextInput(attrs={
        'type':'number',
        'class':'form-control',
        'id':'riwo_sangcho', 
        'name':'riwo_sangcho',
        'step': '.05',
        'min': '0'
    }))

    general_temple_activities = forms.DecimalField(required=False, min_value=0, decimal_places=2, widget=forms.TextInput(attrs={
        'type':'number',
        'class':'form-control',
        'id':'general_temple_activities', 
        'name':'general_temple_activities',
        'step': '.05',
        'min': '0'
    }))

    lamps = forms.DecimalField(required=False, min_value=0, decimal_places=2, widget=forms.TextInput(attrs={
        'type':'number',
        'class':'form-control',
        'id':'lamps', 
        'name':'lamps',
        'step': '.05',
        'min': '0'
    }))

    prayer_flags = forms.DecimalField(required=False, min_value=0, decimal_places=2, widget=forms.TextInput(attrs={
        'type':'number',
        'class':'form-control',
        'id':'prayer_flags', 
        'name':'prayer_flags',
        'step': '.05',
        'min': '0'
    }))

    def send_email(self):
        data = self.cleaned_data

        mail_sended = Offering.send_offering_data_email(data)
        Offering.send_user_confirmation_email(data)

        return mail_sended