from django.shortcuts import render,HttpResponse,redirect


# Create your views here.
def test(request):
    return HttpResponse("<h1>hello world <br> This is My Web</h1>")

def firstweb(request):
    return render(request,'firstweb.html')

def secondpage(request):
    return render(request,'secondpage.html')

def thirdpage(request):
    return render(request,'thirdpage.html')

def home(request):
    return render(request,'home.html')

def product(request):
    return render(request,'product.html')
def idol(request):
    return render(request,'idol.html')

def hny(request):
    return render(request,'hny.html')

def showmydata(request):
    name = "Kittipong"
    surname = "pabuddda"
    gender = "Male"
    status = "Have a Girlfriend"
    work = "Shoppee"
    education = "RMUTI KHONKEAN"
    address = "73 หมู่ 9 ต.โนนจาน อ.บัวลาย จ.นครราชสีมา"
    favorite = "Coding"
    tel = "096-3944908"
    fb = "Kittipong Pabudda"
    pro_list = []
    pro1 = ['เสื้อแมนยู',2800.00,'../../static/image/manuS.jpg']
    pro2 = ['เสื้อลิเวอร์พูล',2800.00,'../../static/image/LFCS.png']
    pro3 = ['เสื้อเชลซี',2790.00,'../../static/image/cfcS.png']
    pro4= ['เสื้อแมนซิตี้',2750.00,'../../static/image/man_cityS.jpg']
    pro5= ['เสื้ออาเซน่อล',2890.00,'../../static/image/asenalS.png']
    pro6=['เสื้อสเปอร์',2590.00,'../../static/image/spurS.jpg']
    pro7=['เสื้อนิวคาสเซิ่ล',2450.00,'../../static/image/newcastleS.jpeg']
    pro8 = ['เสื้อเวสต์แฮม',2450.00,'../../static/image/westham.png']
    pro9=['เสื้อไบร์ตัน',2350.00,'../../static/image/brightonS.jpg']
    pro10=['เสื้อเลสเตอร์',2500.00,'../../static/image/LeicesterS.jpg']
    pro_list.append(pro1)
    pro_list.append(pro2)
    pro_list.append(pro3)
    pro_list.append(pro4)
    pro_list.append(pro5)
    pro_list.append(pro6)
    pro_list.append(pro7)
    pro_list.append(pro8)
    pro_list.append(pro9)
    pro_list.append(pro10)
    context = {'name':name,'surname':surname,'gender':gender,'status':status,'work':work,'education':education
                   ,"address":address,'favorite':favorite,'tel':tel,'fb':fb,'pro_list':pro_list}
    return render(request,'showmydata.html',context)

from ProfileApp.models import Product,product
product_list = []
def showProduct(request):

    context = {'product':product_list}
    return render(request,'showOurProduct.html',context)


def newProduct(request):
    if request.method == 'POST':
        id = request.POST['id']
        name = request.POST['name']
        brand = request.POST['brand']
        price = request.POST['price']
        net = request.POST['net']
        product = Product(id,name,brand,price,net)
        product_list.append(product)
        return redirect('showOurproduct')
    else:
        return render(request,'frmProductNormal.html')

from ProfileApp.forms import *
def frmproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get('id')
            name = form.get('name')
            brand=form.get('brand')
            price = form.get('price')
            net = form.get('net')
            made = form.get('made')
            product = Product(id,name,brand,price,net,made)
            product_list.append(product)
            return redirect('showOurproduct')
        else:
            form = ProductForm(form)
    else:
        form = ProductForm()
    context={"form":form}
    return render(request, 'frmProduct.html',context)

lstOutProduct = []


def listProduct(request):

    context = {'product':lstOutProduct}
    return render(request,'listProduct.html',context)
def inputProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get('id')
            name = form.get('name')
            brand = form.get('brand')
            price = form.get('price')
            amount = form.get('amount')
            made = form.get('made')
            total = price * amount
            if amount < 3:
                discount = 0
            elif amount <= 5:
                discount = total * 0.05
            else:
                discount = total * 0.10
            net = total - discount
            product = Product(id, name, brand, price, amount, made,total,discount,net)
            lstOutProduct.append(product)
            return redirect('listProduct')
        else:
            form = ProductForm(form)
    else:
        form = ProductForm()
    context = {"form": form}
    return render(request, 'inputProduct.html', context)

from ProfileApp.models import product
pro = product
def product_retriveAll(request):
    products = pro.objects.all()
    context = {'products':products}
    return  render(request, 'products/pro_retriveAll.html', context)


def product_retriveOne(request,pid):
    product = pro.objects.get(pid =pid)
    context = {"product":product}
    return  render(request, 'products/pro_retriveOne.html', context)


def createProduct(request):
    if request.method == 'POST':
        form = ProductMForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pro_retriveAll')
    else:
        form = ProductMForm
        context = {'form':form}
        return render(request,'products/createProduct.html',context)


