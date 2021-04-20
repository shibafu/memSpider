from django import forms

SAMPLE_CHOICE =(
    ('1', '1:saa'),
    ('2', '2:ss'),
    ('3', '3:ss')
)


class HelloForm(forms.Form):
    id = forms.IntegerField(label='ID')
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    age = forms.IntegerField(label='age')
    gender = forms.BooleanField(label='gender')
    birthday = forms.DateField(label='birthday')
    '''
    #selectable = forms.ChoiceField(label='select',
                                widget=forms.Select,
                                choices=(
                                    ('1', '1:saa'),
                                    ('2', '2:ss'),
                                    ('3', '3:ss')
                                    )
    )
    '''
    '''
    radioButton = forms.ChoiceField(label='radio',
                                widget=forms.RadioSelect,
                                choices=(
                                    ('1', '1:saa'),
                                    ('2', '2:ss'),
                                    ('3', '3:ss')
                                    )
    )
    '''
    '''
    choiceListButton = forms.MultipleChoiceField(label='radio',
                                widget=forms.SelectMultiple(attrs={'size': 3}),
                                choices=(
                                    ('1', '1:saa'),
                                    ('2', '2:ss'),
                                    ('3', '3:ss')
                                    )
    )
    '''