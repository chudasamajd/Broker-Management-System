from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyC2yNHim8NuOyJrTKxW_zaCML9CO55uYS4",
    'authDomain': "brokersystem-f45eb.firebaseapp.com",
    'projectId': "brokersystem-f45eb",
    'storageBucket': "brokersystem-f45eb.appspot.com",
    'messagingSenderId': "956492884368",
    'appId': "1:956492884368:web:100f4c088f48a56ccdab15",
    'databaseURL':"https://brokersystem-f45eb-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()

user = ''

def index(HttpRequest):
    global user
    return render(HttpRequest,'index.html',{'user':user})

def about(HttpRequest):
    global user
    return render(HttpRequest,'about.html',{'user':user})

def contact(HttpRequest):
    global user
    return render(HttpRequest,'contact.html',{'user':user})

def contactData(HttpRequest):
    uname = HttpRequest.POST.get('name')
    uemail = HttpRequest.POST.get('email')
    subject = HttpRequest.POST.get('subject')
    message = HttpRequest.POST.get('message')

    db.child('query').push(
        {'User Name': uname, 'User Email': uemail, 'Subject': subject, 'Message': message})
    return HttpResponse('Query Submitted Successfully')

def registration(HttpRequest):
    return render(HttpRequest, 'registration.html')

def registrationdata(HttpRequest):
    uname = HttpRequest.POST.get('name')
    password = HttpRequest.POST.get('password')
    gender = HttpRequest.POST.get('gender')
    mail = HttpRequest.POST.get('mail')
    phone = HttpRequest.POST.get('phone')
    address = HttpRequest.POST.get('address')
    dob = HttpRequest.POST.get('dob')
    db.child('registration').push(
        {'Name': uname, 'Password': password, 'Gender': gender, 'E-mail': mail,
         'Phone number': phone, 'Address': address, 'DOB': dob})
    auth.create_user_with_email_and_password(mail,password)
    return render(HttpRequest, 'registration.html',{'data':1})

def login(HttpRequest):
    return render(HttpRequest, 'login.html')

def loginData(HttpRequest):
    global user
    uemail = HttpRequest.POST.get('mail')
    password = HttpRequest.POST.get('password')
    try:
        user = auth.sign_in_with_email_and_password(uemail,password)
        print(user['email'])
        return render(HttpRequest, 'index.html',{'user':user})
    except:
        return render(HttpRequest,'login.html',{'data':1})

def logout(HttpRequest):
    global user
    user = ''
    return render(HttpRequest, 'index.html', {'user': user})

def forsell(HttpRequest):
    global user
    if user:
        return render(HttpRequest,'for sell.html',{'user':user})
    else:
        return render(HttpRequest, 'login.html')

def forselldata(HttpRequest):
    land = HttpRequest.POST.get('land')
    building = HttpRequest.POST.get('building')
    area = HttpRequest.POST.get('area')
    areasq = HttpRequest.POST.get('areasq')
    location = HttpRequest.POST.get('location')
    upper = HttpRequest.POST.get('upper')
    lower = HttpRequest.POST.get('lower')
    sellername = HttpRequest.POST.get('sellername')
    selleraddress = HttpRequest.POST.get('selleraddress')
    sellercontact = HttpRequest.POST.get('sellercontact')
    comment = HttpRequest.POST.get('comment')
    imgurl = HttpRequest.POST.get('imgurl')

    db.child('For Sell').push(
        {'Land Type': land, 'Building Type': building, 'Area Type': area, 'Area': areasq,
         'Location': location, 'Upper': upper, 'Lower': lower, 'Seller Name':sellername,'Seller Address':selleraddress,'Seller Contact':sellercontact,'Comment':comment,'imgurl':imgurl})
    return render(HttpRequest, 'for sell.html', {'data': 1})

def forrent(HttpRequest):
    global user
    if user:
        return render(HttpRequest,'for rent.html',{'user':user})
    else:
        return render(HttpRequest, 'login.html')

def forrentdata(HttpRequest):
    land = HttpRequest.POST.get('land')
    building = HttpRequest.POST.get('building')
    area = HttpRequest.POST.get('area')
    areasq = HttpRequest.POST.get('areasq')
    location = HttpRequest.POST.get('location')
    upper = HttpRequest.POST.get('upper')
    lower = HttpRequest.POST.get('lower')
    sellername = HttpRequest.POST.get('sellername')
    selleraddress = HttpRequest.POST.get('selleraddress')
    sellercontact = HttpRequest.POST.get('sellercontact')
    comment = HttpRequest.POST.get('comment')
    imgurl = HttpRequest.POST.get('imgurl')

    db.child('For Rent').push(
        {'Land Type': land, 'Building Type': building, 'Area Type': area, 'Area': areasq,
         'Location': location, 'Upper': upper, 'Lower': lower, 'Renter Name':sellername,'Renter Address':selleraddress,'Renter Contact':sellercontact,'Comment':comment,'imgurl':imgurl})
    return render(HttpRequest, 'for rent.html', {'data': 1})


def buy(HttpRequest):
    global user
    data = db.child('For Sell').shallow().get()
    sid = []
    land_type = []
    building_type = []
    area_type = []
    area = []
    location = []
    upper_price = []
    lower_price = []
    ownername = []
    owneraddress = []
    contact_no = []
    image = []
    comment = []
    for d in data.val():
        sid.append(d)
        land_type.append(db.child('For Sell').child(d).child('Land Type').get().val())
        building_type.append(db.child('For Sell').child(d).child('Building Type').get().val())
        area_type.append(db.child('For Sell').child(d).child('Area Type').get().val())
        area.append(db.child('For Sell').child(d).child('Area').get().val())
        location.append(db.child('For Sell').child(d).child('Location').get().val())
        upper_price.append(db.child('For Sell').child(d).child('Upper').get().val())
        lower_price.append(db.child('For Sell').child(d).child('Lower').get().val())
        ownername.append(db.child('For Sell').child(d).child('Seller Name').get().val())
        owneraddress.append(db.child('For Sell').child(d).child('Seller Address').get().val())
        contact_no.append(db.child('For Sell').child(d).child('Seller Contact').get().val())
        image.append(db.child('For Sell').child(d).child('imgurl').get().val())
        comment.append(db.child('For Sell').child(d).child('Comment').get().val())

    maindata = zip(sid, land_type, building_type, area_type, area, location, upper_price, lower_price, ownername,
                   owneraddress, contact_no, image, comment)

    return render(HttpRequest,'buy property.html',{'user':user,'data':maindata})

def buySingle(HttpRequest,pid):
    global user
    land_type = []
    building_type = []
    area_type = []
    area = []
    location = []
    upper_price = []
    lower_price = []
    ownername = []
    owneraddress = []
    contact_no = []
    image = []
    comment = []

    land_type.append(db.child('For Sell').child(pid).child('Land Type').get().val())
    building_type.append(db.child('For Sell').child(pid).child('Building Type').get().val())
    area_type.append(db.child('For Sell').child(pid).child('Area Type').get().val())
    area.append(db.child('For Sell').child(pid).child('Area').get().val())
    location.append(db.child('For Sell').child(pid).child('Location').get().val())
    upper_price.append(db.child('For Sell').child(pid).child('Upper').get().val())
    lower_price.append(db.child('For Sell').child(pid).child('Lower').get().val())
    ownername.append(db.child('For Sell').child(pid).child('Seller Name').get().val())
    owneraddress.append(db.child('For Sell').child(pid).child('Seller Address').get().val())
    contact_no.append(db.child('For Sell').child(pid).child('Seller Contact').get().val())
    image.append(db.child('For Sell').child(pid).child('imgurl').get().val())
    comment.append(db.child('For Sell').child(pid).child('Comment').get().val())


    maindata = zip(land_type, building_type, area_type, area, location, upper_price, lower_price, ownername,
                   owneraddress, contact_no, image, comment)

    return render(HttpRequest,'buy property single.html',{'user':user,'data':maindata,'pid':pid})

def purchaseRequest(HttpRequest):
    global user

    pid = HttpRequest.POST.get('pid')
    uname = HttpRequest.POST.get('uname')
    email = HttpRequest.POST.get('email')
    message = HttpRequest.POST.get('message')

    db.child('Purchase Request').push({'Property Id':pid,'User Name':uname, 'Email':email, 'Message': message})
    return render(HttpRequest,'purchase request.html',{'user':user})

def rent(HttpRequest):
    global user
    data = db.child('For Rent').shallow().get()
    sid = []
    land_type = []
    building_type = []
    area_type = []
    area = []
    location = []
    upper_price = []
    lower_price = []
    ownername = []
    owneraddress = []
    contact_no = []
    image = []
    comment = []
    for d in data.val():
        sid.append(d)
        land_type.append(db.child('For Rent').child(d).child('Land Type').get().val())
        building_type.append(db.child('For Rent').child(d).child('Building Type').get().val())
        area_type.append(db.child('For Rent').child(d).child('Area Type').get().val())
        area.append(db.child('For Rent').child(d).child('Area').get().val())
        location.append(db.child('For Rent').child(d).child('Location').get().val())
        upper_price.append(db.child('For Rent').child(d).child('Upper').get().val())
        lower_price.append(db.child('For Rent').child(d).child('Lower').get().val())
        ownername.append(db.child('For Rent').child(d).child('Renter Name').get().val())
        owneraddress.append(db.child('For Rent').child(d).child('Renter Address').get().val())
        contact_no.append(db.child('For Rent').child(d).child('Renter Contact').get().val())
        image.append(db.child('For Rent').child(d).child('imgurl').get().val())
        comment.append(db.child('For Rent').child(d).child('Comment').get().val())

    maindata = zip(sid, land_type, building_type, area_type, area, location, upper_price, lower_price, ownername,
                   owneraddress, contact_no, image, comment)

    return render(HttpRequest,'rent property.html',{'user':user,'data':maindata})

def rentSingle(HttpRequest,pid):
    global user
    land_type = []
    building_type = []
    area_type = []
    area = []
    location = []
    upper_price = []
    lower_price = []
    ownername = []
    owneraddress = []
    contact_no = []
    image = []
    comment = []

    land_type.append(db.child('For Rent').child(pid).child('Land Type').get().val())
    building_type.append(db.child('For Rent').child(pid).child('Building Type').get().val())
    area_type.append(db.child('For Rent').child(pid).child('Area Type').get().val())
    area.append(db.child('For Rent').child(pid).child('Area').get().val())
    location.append(db.child('For Rent').child(pid).child('Location').get().val())
    upper_price.append(db.child('For Rent').child(pid).child('Upper').get().val())
    lower_price.append(db.child('For Rent').child(pid).child('Lower').get().val())
    ownername.append(db.child('For Rent').child(pid).child('Renter Name').get().val())
    owneraddress.append(db.child('For Rent').child(pid).child('Renter Address').get().val())
    contact_no.append(db.child('For Rent').child(pid).child('Renter Contact').get().val())
    image.append(db.child('For Rent').child(pid).child('imgurl').get().val())
    comment.append(db.child('For Rent').child(pid).child('Comment').get().val())


    maindata = zip(land_type, building_type, area_type, area, location, upper_price, lower_price, ownername,
                   owneraddress, contact_no, image, comment)

    return render(HttpRequest,'rent property single.html',{'user':user,'data':maindata,'pid':pid})

def rentRequest(HttpRequest):
    global user

    pid = HttpRequest.POST.get('pid')
    uname = HttpRequest.POST.get('uname')
    email = HttpRequest.POST.get('email')
    message = HttpRequest.POST.get('message')

    db.child('Rent Request').push({'Property Id':pid,'User Name':uname, 'Email':email, 'Message': message})
    return render(HttpRequest,'rent request.html',{'user':user})

def profile(HttpRequest):
    global user

    if user:
        users_data = db.child("registration").order_by_child("E-mail").equal_to(user['email']).get()

        print(users_data)
        return render(HttpRequest, 'profile.html', {'user': user})
    else:
        return render(HttpRequest, 'login.html')

