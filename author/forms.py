from django import forms
from author.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'age', 'id_num']

    def clean_id_num(self):
        id_num = self.cleaned_data.get('id_num')
        if Author.objects.filter(id_num=id_num).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("This ID number is already in use.")
        return id_num
