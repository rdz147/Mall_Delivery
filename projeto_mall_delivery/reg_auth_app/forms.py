from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Consumidor, Lojista

#form de cadastro de consumidor
class CreateConsumidorForm(UserCreationForm):
    class Meta:
        model = Consumidor
        fields = ['username', 'email', 'cpf', 'telefone']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Insira seu nome de usuário'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Insira seu e-mail'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'Insira seu CPF'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Insira seu telefone'}),
        }

#form de cadastro de lojista
class CreateLojistaForm(UserCreationForm):
    class Meta:
        model = Lojista
        fields = ['username', 'email', 'cpf', 'cep', 'endereco', 'cnpj', 'razao_social']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Insira seu nome de usuário'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Insira seu e-mail'}),
            'cpf': forms.TextInput(attrs={'placeholder': 'Insira seu CPF'}),
            'cep': forms.TextInput(attrs={'placeholder': 'Insira o CEP da sua loja'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Insira o endereço da sua loja'}),
            'cnpj': forms.TextInput(attrs={'placeholder': 'Insira o CNPJ da sua loja'}),
            'razao_social': forms.TextInput(attrs={'placeholder': 'Insira a razão social da loja'}),
        }

#form de login
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Nome de usuário'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Senha'}))

#uma das diferenças aqui é que o UserCreationForm trata as senhas de maneira mais segura, salvando apenas o hash no banco