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

class Cadastroforms(forms.Form):
    nome_cadastro = forms.CharField(
        label = "Nome de Cadastro",
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Paulo Ferreira"
            }
        )
    ) 
    email_cadastro = forms.EmailField(
        label = "Email",
        required = True,
        max_length = 100,
        widget = forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: jpferreira@xpto.com"
            }
        )
    )
    senha_1 = forms.CharField(
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
    senha_2 = forms.CharField(
        label = "Confirme sua senha",
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )
