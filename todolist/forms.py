from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=45,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter Tasks',
                'arial-label' : 'ToDo',
                'aria-describedby' : 'add-btn'
            }
        )
    )