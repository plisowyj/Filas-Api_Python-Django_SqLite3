from multiprocessing import Value
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from admin_turnos.models import Tramites, Clientes, Ingresos

class CustomLoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs.update(
        {'class': 'form-control text-uppercase'}
    )
    self.fields['password'].widget.attrs.update(
        {'class': 'form-control '}
    )


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2', 'first_name', 'last_name']

    username = forms.CharField(label='Usuario', min_length=5, max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Clave', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Clave confirmación', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombre', min_length=1, max_length=50)
    last_name= forms.CharField(label='Apellido', min_length=1, max_length=50)

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['username'].widget.attrs.update(
          {'class': 'form-control text-uppercase'}
      )
      self.fields['email'].widget.attrs.update(
          {'class': 'form-control text-uppercase'}
      )
      self.fields['password1'].widget.attrs.update(
          {'class': 'form-control'}
      )
      self.fields['password2'].widget.attrs.update(
          {'class': 'form-control'}
      )
      self.fields['first_name'].widget.attrs.update(
          {'class': 'form-control text-uppercase'}
      )
      self.fields['last_name'].widget.attrs.update(
          {'class': 'form-control text-uppercase'}
      )

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("El usaurio ya existe!")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError("El Email ya existe!")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las claves no coinciden!")
        return password2


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Usuario', min_length=5, max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Clave', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Clave confirmación', widget=forms.PasswordInput)

    
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['username'].widget.attrs.update(
          {'class': 'form-control text-uppercase'}
      )
      self.fields['email'].widget.attrs.update(
          {'class': 'form-control text-uppercase'}
      )
      self.fields['password1'].widget.attrs.update(
          {'class': 'form-control'}
      )
      self.fields['password2'].widget.attrs.update(
          {'class': 'form-control'}
      )

    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("El usaurio ya existe!")
        return username

    def email_clean(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError("El Email ya existe!")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Las claves no coinciden!")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

class CustomTramitesForm(forms.ModelForm):
    class Meta:
        model = Tramites
        fields = ['descripcion', 'activo', 'decorador', 'lugar']
    
    value_active = (
        ('S', 'SI'),
        ('N', 'NO'),
    )

    descripcion = forms.CharField(label='Descripción', min_length=5, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control text-uppercase'}))
    activo = forms.CharField(widget=forms.Select(choices=value_active, attrs={'class': 'form-control text-uppercase'}))
    decorador = forms.CharField(label='Decorador', max_length=1, widget=forms.TextInput(attrs={'class': 'form-control text-uppercase'}))
    lugar = forms.CharField(label='Lugar', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control text-uppercase'}))


class CustomClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['apellido', 'nombres', 'documento', 'fec_nac', 'picture']

    apellido = forms.CharField(label='Apellido *', min_length=1, max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control text-uppercase'}))
    nombres = forms.CharField(label='Nombres *', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control text-uppercase'}))
    documento = forms.CharField(label='N° Documento *', max_length=11, widget=forms.NumberInput(
        attrs={'class': 'form-control text-uppercase'}))
    fec_nac = forms.DateField(label='Fecha Nacimiento *', widget=forms.DateInput(
        attrs={'class': 'form-control'}))
    picture = forms.ImageField(label='Foto *')
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['picture'].widget.attrs.update(
            {'class': 'btn btn-secondary'})
        

    def documento_clean(self):
        documento = self.cleaned_data['documento'].lower()
        new = User.objects.filter(documento=documento)
        if new.count():
            raise ValidationError("El documento ya existe!")
        return documento

    
class CustomTramitesForm(forms.ModelForm):
    class Meta:
        model = Tramites
        fields = ['descripcion', 'activo', 'decorador', 'lugar']

    value_active = (
        ('S', 'SI'),
        ('N', 'NO'),
    )

    descripcion = forms.CharField(label='Descripción', min_length=5, max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control text-uppercase'}))
    activo = forms.CharField(widget=forms.Select(
        choices=value_active, attrs={'class': 'form-control text-uppercase'}))
    decorador = forms.CharField(label='Decorador', max_length=1, widget=forms.TextInput(
        attrs={'class': 'form-control text-uppercase'}))
    lugar = forms.CharField(label='Lugar', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control text-uppercase'}))


class CustomClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['apellido', 'nombres', 'documento', 'fec_nac', 'picture']

    apellido = forms.CharField(label='Apellido *', min_length=1, max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control text-uppercase'}))
    nombres = forms.CharField(label='Nombres *', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control text-uppercase'}))
    documento = forms.CharField(label='N° Documento *', max_length=11, widget=forms.NumberInput(
        attrs={'class': 'form-control text-uppercase'}))
    fec_nac = forms.DateField(label='Fecha Nacimiento *', widget=forms.DateInput(
        attrs={'class': 'form-control'}))
    picture = forms.ImageField(label='Foto *')
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['picture'].widget.attrs.update(
            {'class': 'btn btn-secondary'})
        

    def documento_clean(self):
        documento = self.cleaned_data['documento'].lower()
        new = User.objects.filter(documento=documento)
        if new.count():
            raise ValidationError("El documento ya existe!")
        return documento

    
class CustomTramitesForm(forms.ModelForm):
    class Meta:
        model = Tramites
        fields = ['descripcion', 'activo', 'decorador', 'lugar']

    value_active = (
        ('S', 'SI'),
        ('N', 'NO'),
    )

    descripcion = forms.CharField(label='Descripción', min_length=5, max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control text-uppercase'}))
    activo = forms.CharField(widget=forms.Select(
        choices=value_active, attrs={'class': 'form-control text-uppercase'}))
    decorador = forms.CharField(label='Decorador', max_length=1, widget=forms.TextInput(
        attrs={'class': 'form-control text-uppercase'}))
    lugar = forms.CharField(label='Lugar', max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control text-uppercase'}))


class RecCustomClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['apellido', 'nombres', 'documento', 'fec_nac']

    apellido = forms.CharField(label='Apellido *', min_length=1, max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control text-uppercase'}))
    nombres = forms.CharField(label='Nombres *', max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control text-uppercase'}))
    documento = forms.CharField(label='N° Documento *', max_length=11, widget=forms.NumberInput(
        attrs={'class': 'form-control text-uppercase'}))
    fec_nac = forms.DateField(label='Fecha Nacimiento *', widget=forms.DateInput(
        attrs={'class': 'form-control'}))
    
    def documento_clean(self):
        documento = self.cleaned_data['documento'].lower()
        new = User.objects.filter(documento=documento)
        if new.count():
            raise ValidationError("El documento ya existe!")
        return documento


class FinderApellido(forms.Form):
    apellido = forms.CharField(label='Apellido a buscar', min_length=1, max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control text-uppercase'}))
