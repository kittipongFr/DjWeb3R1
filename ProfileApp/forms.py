from django.forms import *

class ProductForm(Form):
    BRAND_LIST=[('Acer','Acer'),('Hp','Hp'),('Lenovo','Lenovo'),('Asus','Asus')]
    MADE_LIST = [('Thai','Thai'),('China','China')]
    id = CharField(max_length=13,label="รหัสสินค้า",required=True,
                          widget=TextInput(attrs={'size':'15'}))
    name = CharField(max_length=50, label="ชื่อสินค้า", required=True,
                          widget=TextInput(attrs={'size': '15'}))
    brand = ChoiceField( label="ยี่ห้อสินค้า", required=True,
                          widget=Select, choices=BRAND_LIST)
    price = FloatField(min_value=1.00,max_value=10000.00, label="ราคาต่อหน่วย", required=True,
                          widget=NumberInput(attrs={'size': '15'}))
    net = IntegerField(min_value=0,max_value=1000, label="คงเหลือ", required=True,
                          widget=NumberInput(attrs={'size': '15'}))
    made = ChoiceField(label="ผลิตจาก", required=True,
                        widget=RadioSelect, choices=MADE_LIST)
