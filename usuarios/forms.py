from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'EX.: João Silva'

        })
    )
    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'EX.: João Silva'

        })
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
          attrs={
            'class': 'form-control',
            'placeholder': 'EX.: joao@gmail.com'
            }  
        )
    )

    senha_1=forms.CharField(
            label='Senha',
            required=True,
            max_length=70,
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Digite sua senha'
            }
        )
    )
    senha_2=forms.CharField(
        label='Digite a senha novamente',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )


    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Não pode ter espaços no nome de usuário')
            else:
                return nome 