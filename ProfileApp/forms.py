from django.forms import *

class ProductForm(Form):
    BRAND_LIST=[('Nike','Nike'),('Adidas','Adidas'),('Puma','Puma')]
    MADE_LIST = [('Thai','Thai'),('USA','USA')]
    NAME_LIST = [('Mancester United', 'Mancester United'), ('Liverpool', 'Liverpool'), ('Chelsea', 'Chelsea'),
                 ('Asenal','Asenal'),('Mancester City','Mancester City')]
    id = CharField(max_length=13,label="รหัสสินค้า",required=True,
                          widget=TextInput(attrs={'size':'15'}))
    name = ChoiceField( label="ชื่อสินค้า", required=True,
                          widget=Select,choices=NAME_LIST)
    brand = ChoiceField( label="ยี่ห้อสินค้า", required=True,
                          widget=Select, choices=BRAND_LIST)
    price = FloatField(min_value=1.00,max_value=10000.00, label="ราคาต่อหน่วย", required=True,
                          widget=NumberInput(attrs={'size': '15'}))
    amount = IntegerField(min_value=0,max_value=1000, label="คงเหลือ", required=True,
                          widget=NumberInput(attrs={'size': '15'}))
    made = ChoiceField(label="ผลิตจาก", required=True,
                        widget=RadioSelect, choices=MADE_LIST)
from .models import *
class ProductMForm(ModelForm):
    class Meta:
        model = product
        fields = ('pid','name','brand','price','net','category')
        widgets = {
            'pid':TextInput(attrs={'class':'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'brand': TextInput(attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control'}),
            'net': NumberInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
        }
        labels={
            'pid':'รหัสสินค้า',
            'name':'ชื่อสินค้า',
            'brand':'ยี่ห้อ',
            'price':'ราคา',
            'net':'คงเหลือ',
            'category':'ประเภท',
        }

