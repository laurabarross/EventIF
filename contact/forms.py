from django import forms


class ContatoForm(forms.Form):
    name = forms.CharField(label='Nome')

    phone = forms.CharField(label='Telefone',
       required=False, 
       widget=forms.TextInput(attrs={'placeholder': 'Opcional'}))
    
    email = forms.EmailField(label='Email')

    message = forms.CharField(label = 'Message', widget=forms.Textarea())

