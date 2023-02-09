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
        fields = ('name','brand','price','net','category')
        widgets = {

            'name': TextInput(attrs={'class': 'form-control'}),
            'brand': TextInput(attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control'}),
            'net': NumberInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
        }
        labels={

            'name':'ชื่อสินค้า',
            'brand':'ยี่ห้อ',
            'price':'ราคา',
            'net':'คงเหลือ',
            'category':'ประเภท',
        }
    # def UpdateForm(self):
    #     self.fields['pid'].widget.attrs['readonly']=True
    #     self.fields['pid'].label= 'รหัสสินค้าแก้ไขไม่ได้'


class ProductUpdateMForm(ModelForm):

    class Meta:

        model = product
        fields = ('name','brand','price','net','category')
        widgets = {
            # 'pid':TextInput(attrs={'class':'form-control','readonly': 'readonly'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'brand': TextInput(attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control'}),
            'net': NumberInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
        }
        labels={
            # 'pid':'รหัสสินค้า',
            'name':'ชื่อสินค้า',
            'brand':'ยี่ห้อ',
            'price':'ราคา',
            'net':'คงเหลือ',
            'category':'ประเภท',
        }

class GoodsMForm(ModelForm):
    class Meta:
        model = Goods
        fields = ('gid','name','brand','model','price','net','goodscategory','property')
        widgets = {
            'gid':TextInput(attrs={'class':'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'brand': TextInput(attrs={'class': 'form-control'}),
            'price': NumberInput(attrs={'class': 'form-control'}),
            'net': NumberInput(attrs={'class': 'form-control'}),
            'model':  TextInput(attrs={'class': 'form-control'}),
            'goodscategory': Select(attrs={'class': 'form-control'}),
            'property':TextInput(attrs={'class': 'form-control'}),
        }
        labels={
            'gid':'รหัสสินค้า',
            'name':'ชื่อสินค้า',
            'brand':'ยี่ห้อ',
            'model':'รุ่น',
            'price':'ราคา',
            'net':'คงเหลือ',
            'category':'ประเภท',
            'property': 'รายละเอียด',
        }
    def UpdateGoodsForm(self):
        self.fields['gid'].widget.attrs['readonly']=True
        self.fields['gid'].label= 'รหัสสินค้าแก้ไขไม่ได้'

class CusMForm(ModelForm):
    class Meta:
        GENDER_LIST = [( True,'ชาย'), (False,'หญิง')]
        model = Customer
        fields = ('cid','name','surname','address','telephone','gender','carreer','password')
        widgets = {
            'cid':TextInput(attrs={'class':'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'surname': TextInput(attrs={'class': 'form-control'}),
            'address': Textarea(attrs={'class': 'form-control'}),
            'telephone': NumberInput(attrs={'class': 'form-control'}),
            'gender':   Select(attrs={'class': 'form-control'},choices=GENDER_LIST),
            'carreer': TextInput(attrs={'class': 'form-control'}),
            'password':TextInput(attrs={'class': 'form-control'}),
        }
        labels={
            'cid':'รหัสลูกค้า',
            'name':'ชื่อลูกค้า',
            'surname':'นามสกุล',
            'address':'ที่อยู่',
            'telephone':'โทร',
            'gender':'เพศ',
            'carreer':'อาชีพ',
            'password': 'รหัสผ่าน',
        }
    def UpdateCusForm(self):
        self.fields['cid'].widget.attrs['readonly']=True
        self.fields['cid'].label= 'รหัสสินค้าแก้ไขไม่ได้'
