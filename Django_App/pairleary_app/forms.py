from django import forms
# ↑Django formsのインポート・↓Postモデルのインポート”POST”でOK？
from .models import Orders

# ModelForm だとDjangoに伝える記述
class CreateOrder(forms.ModelForm):

# フォームフィールドに置く物の指定
    class Meta:
        model = Orders
        fields = "__all__"
        
        