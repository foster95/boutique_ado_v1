from django import forms
from .models import Product, Category

clsss ProductForm(forms.ModelForm):
    """Form for adding and updating products."""
    class Meta:
        model = Product
        fields = [
            __all__,
        ]
    
    def init__(self, *args, **kwargs):
        """Add classes to form fields."""
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names

        for field_name in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'