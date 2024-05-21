from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from user.forms import SignUpForm
from django.contrib import messages
import bcrypt
from django.http import *
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from .models import User,antena
from .models import *
from django.core.files.storage import FileSystemStorage
import csv
import qrcode
from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item, Transaction
from pyinvoice.templates import SimpleInvoice

# Create your views here.

class store:
    x=1
    c=0
    b=0
    userno=1
    empid=10
    comno=10
    invno=0
    mm=""
    ss=""


def page1(request):
    return render(request, "webpage/page01.html")

def page2(request):
    return render(request, "webpage/page02.html")

def page4(request):
    return render(request,"webpage/page04.html")

def page9(request):
    return render(request, "webpage/page09.html")


def page6(request):
    return render(request, "webpage/page06.html")

def page6c(request):
    return render(request, "webpage/page06c.html")

def page10(request):
    return render(request, "webpage/page10.html")

def about(request):
	return render(request, "webpage/about.html")


def contact(request):
	return render(request, "webpage/contact.html")


def sendBack(request):
    return render(request,"webpage/page02.html")

def emplanding(request):
    print(store.empid)
    return render(request,"webpage/page13.html",{'empid':store.empid})


def returndetails(request):
    #x = ditems.invoice_no
    #var2 = antena.objects.raw('select * from user_antena where invoice_no_id=1234')
    ditems = Invoice.objects.filter(invoice_no=store.x)[0]
    var2 = antena.objects.filter(invoice_no_id=ditems.invoice_no)
    
def lala(request):
    g = Complain.objects.filter(uid_id=store.userno)
    return render(request, "webpage/page04.html",{'g':g})

def peyechi(request):
    y=request.GET['dadu']
    z=request.GET['dadu1']
    w=request.GET['dadu2']
    con={}
    con['item_no']=y    
    con['item_qty']=z
    con['item_price']=w
    return render(request,'webpage/page05.html',{'con':con})
    #return HttpResponse("<h1>yes</h1>")

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    #hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=request.POST['password'], email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/success')

def login(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        
        #if (bcrypt.checkpw(user.password.encode(),request.POST['login_password'].encode() )):
        if(user.password==request.POST['login_password']):
            request.session['id'] = user.id
            store.userno=user.id
            return redirect('/lala')
    return redirect('/')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'webpage/success.html', context)


def search(request):
    temp=CustomerInvoice.objects.filter(c_id_id=store.userno)
    l=[]
    for i in temp:
        l.append(i.invoice_no_id)
    y=request.POST['search_oid']
    if int(y) in l:
        ditems = Invoice.objects.filter(invoice_no=request.POST['search_oid'])[0]
        store.x = ditems.invoice_no
        #var2 = antena.objects.raw('select * from user_antena where invoice_no_id=1234')
        var2 = antena.objects.filter(invoice_no_id=ditems.invoice_no)          
        return render(request,'webpage/page03.html',{'ditems':ditems,'var2':var2})
    else:
       return HttpResponse("<h1> order not found </h1>")


def emplogin(request):
    if (Employee.objects.filter(emp_id=request.POST['e_id']).exists()):
        emp = Employee.objects.filter(emp_id=request.POST['e_id'])[0]
        if(emp.emp_password==request.POST['pwd']):
            store.empid=request.POST['e_id']
            return redirect('/emplanding')
    return redirect('/')

def sendmail(request):
    html_content='Event Started'
    notification='Request Recieved'    
    send_mail('Success',html_content,settings.EMAIL_HOST_USER,['rijit.chakraborty10@gmail.com'],fail_silently=False)
    return render(request,"webpage/page02.html")

def attach(request):
    sub = 'Testing attachment'
    body = 'Please do not respond to this message.'
    sender = 'rijitdadubanerjee@gmail.com' 
    reciever = ['asinha231@gmail.com']
    email = EmailMessage(sub,body,sender,reciever)
    email.attach_file('media/schedule.pdf')
    email.send()
    return HttpResponse('Check your mail')

def reason(request):
    return render(request,"webpage/page04.html")

    


def event(request):   
    context = {}
    system = request.POST.get('system', None)
    #context['system'] = system
    print(system)
    return  render(request, 'webpage/page03.html', {'system':system})

def reqlist(request):
    b=customerservice.objects.filter(emp_no=store.empid)
    for i in b:
        #print(i.csr_no)
        z=i.csr_no
    var3 = Complain.objects.filter(csr_no=z)
    #for i in var3:
        #print(i.complain_no)
    return render(request, 'webpage/page08.html',{'var3':var3})


def cslogin(request):
    return render(request,'webpage/page07.html')

def upload(request):
    context={}
    if request.method=='POST':
        uploaded_file = request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        context['url'] = fs.url(name)

    return render(request, 'webpage/upload.html', context)


def uploadc(request):
    context={}
    if request.method=='POST':
        uploaded_file = request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'webpage/uploadc.html', context)

def bhuss(request):
    store.b=request.GET['complainnum']

def fuss(request):
    a=request.GET['add']
    img = complainimages.objects.create(f_path=a, complain_no_id=store.comno)
    img.save()
    return upload(request)

def tuss(request):
    if len(store.mm)==0:
        store.mm=request.GET['add']
        print(store.mm)
    elif len(store.ss)==0:
        store.ss=request.GET['add']
        paint(store.ss)
    return uploadc(request)

def muss(request):
    kk=docs.objects.create(in_path=store.mm,eawaybill_path=store.ss,complain_no_id=store.comno)
    kk.save()
    store.mm=""
    store.ss=""
    return render(request,"webpage/page02.html")

   
    

def huss(request):
    x = complainimages.objects.all()
    for i in x:
        print(i.f_path)
    return render(request,'webpage/download.html',{'x':x})


def boss(request):
    var4 = Complain.objects.filter(csr_no=10)

    return render(request,'webpage/page09.html',{'var4':var4})

def found(request):
    var5={}
    var5['complain_no'] = request.GET['complain_no']
    var5['csr_no'] = request.GET['csr_no']
    var5['uid_id'] = request.GET['uid_id']
    var5['invoice_no_id'] = request.GET['item_no_id']
    var5['item_no_id'] = request.GET['item_no_id']
    var5['item_qty'] = request.GET['item_qty']
    var5['reason'] = request.GET['reason']
    comno=request.GET['complain_no']
    var5['freetext'] = request.GET['freetext']
    print(comno)
    var6=complainimages.objects.filter(complain_no_id=request.GET['complain_no'])
    var7=docs.objects.filter(complain_no_id=request.GET['complain_no'])
    return render(request,'webpage/page09.html',{'var5':var5,'var6':var6,'var7':var7})


def extract1(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    reg = Invoice.objects.all()

    writer = csv.writer(response)
    #writer.writerow(['Last Name', 'First Name', 'email'])
    
    for r in reg:
        print(r.invoice_no)
        print(r.invoice_price)
        print(r.order_date)
        print(r.delivery_date)
        writer.writerow([r.invoice_no,r.invoice_price,r.order_date,r.delivery_date])
    return response


def extract2(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    reg = antena.objects.all()

    writer = csv.writer(response)
    #writer.writerow(['Last Name', 'First Name', 'email'])
    
    for r in reg:
        print(r.item_qty)
        print(r.item_price)
        print(r.invoice_no_id)
        print(r.item_no_id)
        writer.writerow([r.item_qty,r.item_price,r.invoice_no_id,r.item_no_id])
    return response

def extract3(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    reg = Item.objects.all()

    writer = csv.writer(response)
    #writer.writerow(['Last Name', 'First Name', 'email'])
    
    for r in reg:
        print(r.item_no)
        print(r.item_name)
        print(r.item_price)
        writer.writerow([r.invoice_no,r.invoice_price,r.order_date,r.delivery_date])
    return response

def accept(request):

    aa=request.POST['ser']
    print(type(aa))
    if len(aa)==0 or len(bb)==0:
        return HttpResponse("Please Enter the field SER and TER")
    else:
        vox = errornumbers.objects.create(complain_no_id=store.comno, ser_no=aa, ter_no=0,der_no=1,notes="none")
        vox.save()
        obj = Complain.objects.get(complain_no=store.comno)
        obj.status = 'open'
        obj.save()
        sub = 'Request for '+str(store.comno)+' is accepted'
        body = 'Dear customer your return request is accepted. Please visit the portal and upload the  Rejection invoice/delivery Challan and Ewaybill in PDF format.'
        sender = 'rijitdadubanerjee@gmail.com' 
        reciever = ['ad.ankit013@gmail.com']
        email = EmailMessage(sub,body,sender,reciever)
        #email.attach_file('media/schedule.pdf')
        email.send()
        return HttpResponse('Check your mail')
    
def fun(request):
    return HttpResponse('No return possible')


def decline(request):    
    obj = Complain.objects.get(complain_no=store.comno)
    obj.status = 'closed'
    obj.save()
    sub = 'Request for '+str(store.comno)+' is rejected'
    body = 'Please do not respond to this message.'
    sender = 'rijitdadubanerjee@gmail.com' 
    reciever = ['mukherjeeantara24@gmail.com']
    email = EmailMessage(sub,body,sender,reciever)
    #email.attach_file('media/schedule.pdf')
    email.send()
    return HttpResponse('Check your mail')

#def regcomplain(request):
    #vox = Complain.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=request.POST['password'], email=request.POST['email'])
    #vox.save()

def fetch(request):
    print("&&&")
    a=request.GET['a']
    b=request.GET['b']
    c=request.GET['c']
    o_qty=request.GET['o_qty']
    ret_qty=request.GET['ret_qty']
    rcv_qty=request.GET['rcv_qty']
    d=request.GET['d']
    cmmnt=request.GET['cmmnt']
    e=request.GET['e']
    z=custemp.objects.get(c_id_id=store.userno)
    x=int(z.csr_no_id)
    print(x)
    com = Complain.objects.create(csr_no=store.x,uid_id=store.userno,invoice_no_id=x,item_no_id=a,item_qty=b,recieved_qty=rcv_qty,returned_qty=ret_qty,reason=d,notes=cmmnt,grn=e,status="open")
    com.save()
    print(a,b,c,o_qty,ret_qty,rcv_qty,d,cmmnt,e)
    return render(request,'webpage/upload.html')


def goodspeed(request):
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)
    qr.add_data('DADU')
    qr.make(fit=True)
    img = qr.make_image()
    img.save('D:\\im.jpeg')
    return HttpResponse("<h1>Please check your explorer</h1>")


def godspeed(request):
    store.comno=request.POST['bicchu']
    z = Complain.objects.get(complain_no=store.comno)
    a = z.item_no_id
    b = z.returned_qty    
    c = copy.objects.get(item_noo=a)
    print(c.item_noo,c.item_name,c.item_price)
    str1 = "C:\\goodsreturn\\invoices\\"+str(store.comno)+"invoice.pdf"
    doc = SimpleInvoice(str1)

    # Paid stamp, optional
    #doc.is_paid = True
    #doc.invoice_info = InvoiceInfo(1023, datetime.now(), datetime.now())# Invoice info, optional
    # Service Provider Info, optional
    doc.service_provider_info = ServiceProviderInfo(
        name='SKF India Ltd.',
        street='Chinchwad',
        city='Pune',
        state='Maharashtra',
        country='India',
        post_code='411018',
        vat_tax_number='28161826319'
    )

    
    # Client info, optional
    #doc.client_info = ClientInfo(email='client@example.com')

    # Add Item
    doc.add_item(Item(c.item_noo, c.item_name, int(b), c.item_price))
    #doc.add_item(Item('Item 2', 'Item desc', 2, '2.2'))
    #doc.add_item(Item('Item 3', 'Item desc', 3, '3.3'))

    # Tax rate, optional
    #doc.set_item_tax_rate(20)  # 20%

    # Transactions detail, optional
    #doc.add_transaction(Transaction('Paypal', 111, datetime.now(), 1))
    #doc.add_transaction(Transaction('Stripe', 222, date.today(), 2))

    # Optional
    doc.set_bottom_tip("Email: example@example.com<br />Don't hesitate to contact us for any questions.")

    doc.finish()
    return HttpResponse("<h1>Please check your explorer</h1>")


def bothmail(request):
    x=Complain.objects.get(complain_no=store.comno)
    print(x.uid_id)
    y=User.objects.get(id=x.uid_id)
    path="C:\\goodsreturn\\invoices\\"+str(store.comno)+"invoice.pdf"
    sub1 = 'Request for '+str(store.comno)+' is accepted'
    body1 = 'Please do not respond to this message.'
    sender1 = 'rijitdadubanerjee@gmail.com' 
    reciever1 = [y.email]
    email1 = EmailMessage(sub1,body1,sender1,reciever1)
    email1.attach_file(path)
    email1.send()
    sub2 = 'Request for '+str(store.comno)+' is accepted'
    body2 = 'Please do not respond to this message.'
    sender2 = 'rijitdadubanerjee@gmail.com' 
    reciever2 = ['mukherjeeantara24@gmail.com']
    email2 = EmailMessage(sub2,body2,sender2,reciever2)
    email2.attach_file(path)
    email2.send()
    return HttpResponse("Mail sent to customer and transporter")



def index(request):
    x = track.objects.all()
    for i in x:
        print(i.hoos)
    return render(request,"webpage/index.html",{'x':x})