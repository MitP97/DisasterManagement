from django import forms
from django.contrib.auth import login
from django.contrib import auth


SHELTER_TYPE_CHOICES =(
    ('g','government'),
    ('a','ad-hoc'),
)

GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female'),
    ('o', 'Other'),
)

ROLE_CHOICES = (
    ('a', 'Admin'),
    ('o', 'Operator'),
    ('s', 'Supplier'),
)

SUPPLY_TYPE_CHOICES = (
    ('fp','food_packet'),
    ('fa','first_aid'),
    ('b','beddings'),
    ('w','water'),
)

class CivilianRegistrationForm(forms.Form):
    """
    Complete form for civilian registration
    """
    def __init__(self,*args,**kwargs):
        self.system_user=kwargs.pop('system_user',None)
        super(CivilianRegistrationForm,self).__init__(*args,**kwargs)
        self.fields['family_id']=forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'title':'Family ID',
                'class':'form-control'
            }),
            required=False,
        )
        self.fields['aadhar_number']=forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'title':'Aadhar Number',
                'class':'form-control'
            }),
            required=True,
        )
        self.fields['first_name']=forms.CharField(
            max_length=30,
            widget=forms.TextInput(attrs={
                'title':'First Name',
                'class':'form-control'
            }),
        )
        self.fields['middle_name']=forms.CharField(
            max_length=30,
            widget=forms.TextInput(attrs={
                'title':'Middle Name',
                'class':'form-control'
            }),
            required=False,
        )
        self.fields['last_name']=forms.CharField(
            max_length=30,
            widget=forms.TextInput(attrs={
                'title':'Last Name',
                'class':'form-control'
            }),
        )
        self.fields['contact']=forms.CharField(
            max_length=100,
            widget=forms.TextInput(attrs={
                'title':'Contact ',
                'class':'form-control'
            }),
            required=True,
        )
        self.fields['dob']=forms.DateField(
            widget=forms.DateInput(attrs={
                'title':'Date of Birth',
                'class':'form-control'
            }),
            required=True,
        )
        self.fields['gender']=forms.CharField(
            max_length=10,
            widget=forms.Select(choices = GENDER_CHOICES, attrs={
                'title':'Gender',
                'class':'form-control'
            }),
        )
        self.fields['blood_group']=forms.CharField(
            widget=forms.TextInput(attrs={
                'title':'Blood Group',
                'class':'form-control'
            }),
            required=True,
        )
        self.fields['address_line_1']=forms.CharField(
            max_length=100,
            widget=forms.TextInput(attrs={
                'title':'Address Line 1',
                'class':'form-control'
            }),
            required=True,
        )
        self.fields['address_line_2']=forms.CharField(
            max_length=100,
            widget=forms.TextInput(attrs={
                'title':'Address Line 2',
                'class':'form-control'
            }),
            required=False,
        )
        self.fields['address_line_3']=forms.CharField(
            max_length=100,
            widget=forms.TextInput(attrs={
                'title':'Address Line 3 ',
                'class':'form-control'
            }),
            required=False,
        )
        self.fields['city']=forms.CharField(
            max_length=100,
            widget=forms.TextInput(attrs={
                'title':'City',
                'class':'form-control'
            }),
            required=True,
        )
        self.fields['state']=forms.CharField(
            max_length=100,
            widget=forms.TextInput(attrs={
                'title':'State',
                'class':'form-control'
            }),
            required=True,
        )
        self.fields['country']=forms.CharField(
            max_length=100,
            widget=forms.TextInput(attrs={
                'title':'Country',
                'class':'form-control'
            }),
            required=True,
        )
        self.fields['pincode']=forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'title':'Pincode',
                'class':'form-control'
            }),
            required=True,
        )
        self.fields['latitude']=forms.DecimalField(
            widget=forms.NumberInput(attrs={
                'title':'Latitude',
                'class':'form-control'
            }),
            required=True,
        )
        self.fields['longitude']=forms.DecimalField(
            widget=forms.NumberInput(attrs={
                'title':'Longitude',
                'class':'form-control'
            }),
            required=True,
        )

class SystemUserRegistrationForm(forms.Form):
    """
    Complete form for official registration
    """
    def __init__(self,*args,**kwargs):
        self.system_user=kwargs.pop('system_user',None)
        super(SystemUserRegistrationForm,self).__init__(*args,**kwargs)
        self.fields['aadhar_number']=forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'title':'Aadhar Number',
                'class':'form-control'
            }),
            required=True,
        )
        self.fields['password']=forms.CharField(
            widget=forms.PasswordInput(attrs={
                'title':'Password',
                'class':'form-control'
            }),
            required=True,
        )
        self.fields['confirm_password']=forms.CharField(
            widget=forms.PasswordInput(attrs={
                'title':'Confirm Password',
                'class':'form-control'
            }),
            required=True,
        )

    def clean(self):
        cleaned_data = super(SystemUserRegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

class CivilianAtShelterForm(forms.Form):
    """
    Complete form for civilian at shelter
    """
    def __init__(self,*args,**kwargs):
        self.system_user=kwargs.pop('system_user',None)
        super(CivilianAtShelterForm,self).__init__(*args,**kwargs)
        self.fields['aadhar_number']=forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'title':'Aadhar Number',
                'class':'form-control'
            }),
            required=False,
        )
        self.fields['mobile_number']=forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'title':'Mobile Number',
                'class':'form-control'
            }),
            required=False,
        )

    def clean(self):
        cleaned_data = super(CivilianAtShelterForm, self).clean()
        try:
            aadhar_number = cleaned_data.get("aadhar_number")
        except ObjectDoesNotExist:
            pass
        try:
            mobile_number = cleaned_data.get("mobile_number")
        except ObjectDoesNotExist:
            pass
        if (aadhar_number is None) and (mobile_number is None): # both were not entered
            raise forms.ValidationError("Enter either of the data")

        return cleaned_data

class CivilianAllocationForm(forms.Form):
    """
    Complete form for civilian at shelter
    """
    def __init__(self,*args,**kwargs):
        self.system_user=kwargs.pop('system_user',None)
        super(CivilianAllocationForm,self).__init__(*args,**kwargs)
        self.fields['aadhar_number']=forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'title':'Aadhar Number',
                'class':'form-control'
            }),
            required=False,
        )
        self.fields['mobile_number']=forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'title':'Mobile Number',
                'class':'form-control'
            }),
            required=False,
        )
        self.fields['count'] = forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'title':'Total packets given',
                'class':'form-control'
            }),
            required=True,
        )

class LoginForm(forms.Form):
    """
    Complete form for login of system users
    """
    def __init__(self,*args,**kwargs):
        self.system_user=kwargs.pop('system_user',None)
        super(LoginForm,self).__init__(*args,**kwargs)
        self.fields['aadhar_number']=forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'title':'Aadhar Number',
                'class':'form-control'
            }),
            required=True,
        )
        self.fields['password']=forms.CharField(
            widget=forms.PasswordInput(attrs={
                'title':'Password',
                'class':'form-control'
            }),
            required=True,
        )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get("aadhar_number")
        password = cleaned_data.get("password")
        user = auth.authenticate(username=cleaned_data.get('aadhar_number'), password=cleaned_data.get('password'))
        if user is None:
            raise forms.ValidationError("Invalid Login")

        return cleaned_data

class ShelterRegistrationForm(forms.Form):
        def __init__(self,*args,**kwargs):
            self.shelter=kwargs.pop('shelter',None)
            super(ShelterRegistrationForm,self).__init__(*args,**kwargs)
            self.fields['name']=forms.CharField(
                widget=forms.TextInput(attrs={
                    'title':'Name',
                    'class':'form-control'
                }),
                required=True,
            )
            self.fields['total_capacity_of_people']=forms.IntegerField(
                widget=forms.NumberInput(attrs={
                    'title':'Total Capacity Of People',
                    'class':'form-control'
                }),
                required=True,
            )
            self.fields['shelter_latitude']=forms.FloatField(
                widget=forms.NumberInput(attrs={
                    'title':'Latitude',
                    'class':'form-control'
                }),
                required=True,
            )
            self.fields['shelter_longitude']=forms.FloatField(
                widget=forms.NumberInput(attrs={
                    'title':'Longitude',
                    'class':'form-control'
                }),
                required=True,
            )

class SupplierForm(forms.Form):

    def __init__(self,*args,**kwargs):
        self.supplier=kwargs.pop('supplier',None)
        super(SupplierForm,self).__init__(*args,**kwargs)
        self.fields['food_count']=forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'title':'Aadhar Number',
                'class':'form-control'
            }),
            required=False,
        )
        self.fields['first_aid_count']=forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'title':'First Aid',
                'class':'form-control'
            }),
            required=False,
        )
        self.fields['bedding_count']=forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'title':'Bedding',
                'class':'form-control'
            }),
            required=False,
        )
        self.fields['water_count']=forms.IntegerField(
            widget=forms.NumberInput(attrs={
                'title':'Water',
                'class':'form-control'
            }),
            required=False,
        )

        def clean(self):
            cleaned_data = super(SupplierForm, self).clean()
            try:
                food_count = cleaned_data.get("food_count")
            except ObjectDoesNotExist:
                pass
            try:
                first_aid_count = cleaned_data.get("first_aid_count")
            except ObjectDoesNotExist:
                pass
            try:
                bedding_count = cleaned_data.get("bedding_count")
            except ObjectDoesNotExist:
                pass
            try:
                water_count = cleaned_data.get("water_count")
            except ObjectDoesNotExist:
                pass
            if (food_count is None) and (first_aid_count is None) and (bedding_count is None) and (water_count is None):
                raise forms.ValidationError("Invalid Login")

            return cleaned_data
