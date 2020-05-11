from django import forms


class ContactForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
    author = forms.EmailField(label="Votre adresse e-mail")
    

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        return cleaned_data
