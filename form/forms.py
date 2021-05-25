from django import forms

class InputForm(forms.Form):
    Beds = forms.IntegerField(required=True)
    Baths = forms.IntegerField(required=True)
    Cars = forms.IntegerField(required=True)
    Area = forms.FloatField(required=True)
    Date = forms.IntegerField(required=True)
    Lat = forms.FloatField(required=True)
    Long = forms.FloatField(required=True)
    Dis = forms.FloatField(required=True)
    Ptype_CHOICES = [
        ('House', 'House'),
        ('House: One Storey / Lowset', 'House: One Storey / Lowset'),
        ('House: Semi Detached', 'House: Semi Detached'),
        ('House: Two Storey / Highset', 'House: Two Storey / Highset'),
        ('Unit', 'Unit'),
        ('Unit: Standard', 'Unit: Standard'),
        ('Other', 'Other'),
    ]

    Ptype = forms.ChoiceField(choices=Ptype_CHOICES,required=True)

    NSW_CHOICES = [
        ('2112', '2112'),
        ('2114', '2114'),
        ('2118', '2118'),
        ('2119', '2119'),
        ('2120', '2120'),
        ('2122', '2122'),
        ('2126', '2126'),
        ('2151', '2151'),
        ('2152', '2152'),
        ('2153', '2153'),
        ('2154', '2154'),
    ]

    NSW = forms.ChoiceField(choices=NSW_CHOICES,required=True)