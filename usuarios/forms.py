from django import forms

class Loginforms(forms.Form):
    nome_login = forms.CharField(
        label = "Nome de login",
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Paulo Ferreira"
            }
        )
    )
    
    senha = forms.CharField(
        label = "Senha",
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

