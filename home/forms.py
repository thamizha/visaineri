from django.forms import ModelForm
from models import Author

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        exclude = ('user',)
