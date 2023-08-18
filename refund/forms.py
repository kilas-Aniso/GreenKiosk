from django import forms
from .models import Refund
class RefundUploadForm(forms.ModelForm):
    class Meta:
        model= Refund
        fields ="__all__"