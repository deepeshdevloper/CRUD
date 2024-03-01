from django.shortcuts import render
from .models import *
# Create your views here.

#View for Register Page

# hello world


def RegisterPage(request):
    return render(request,"app/register.html")



# View for user registration
def UserRegister(request):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        # First we will validate that user already exist
        user = User.objects.filter(Email=email)
        userno = User.objects.filter(Contact=contact)

        if user: 
            message = "Email already registered"
            return render(request,"app/register.html",{'msg':message})
        elif userno:
            message = "Contact already registered"
            return render(request,"app/register.html",{'msg':message})
        else:
            if password == cpassword:
                newuser = User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                message = "User register Successfully"
                return render(request,"app/login.html",{'msg':message})
            else:
                message = "Password and Confirm Password Does not Match"
                return render(request,"app/register.html",{'msg':message})



#Login VIew

def LoginPage(request):
    return render(request,"app/login.html")


# Login User
def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Checking the emailid with database
        user = User.objects.filter(Email=email)
        if user:
            data = User.objects.get(Email=email)
            if data.Password == password:
                fname = data.Firstname
                lname = data.Lastname
                email = data.Email
                contact = data.Contact
                password = data.Password
                user={
                    'fname':fname,
                    'lname':lname,
                    'email':email,
                    'contact':contact,
                    'password':password,
                }
                return render(request,"app/home.html",{'key':user})
            else:
                message = "Password does not match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message = "User does not exist"
            return render(request,"app/register.html",{'msg':message})
        

def queryinsert(request):
    if request.method == "POST":
        email = request.POST['email']
        query = request.POST['query']
        
        Query.objects.create(
            Email = email,
            Query = query,
        )  
        data1 = Query.objects.filter(Email=email)
        data = User.objects.get(Email=email)
        fname = data.Firstname
        lname = data.Lastname
        email = data.Email
        contact = data.Contact
        password = data.Password
        user={
            'fname':fname,
            'lname':lname,
            'email':email,
            'contact':contact,
            'password':password,
        }
        return render(request,"app/home.html",{'key':user,'data':data1})
    
def queryshow(request,pk):
    print(pk)
    data1 = Query.objects.filter(Email=pk)
    data = User.objects.get(Email=pk)
    fname = data.Firstname
    lname = data.Lastname
    email = data.Email
    contact = data.Contact
    password = data.Password
    user={
        'fname':fname,
        'lname':lname,
        'email':email,
        'contact':contact,
        'password':password,
    }
    return render(request,"app/home.html",{'key':user,'data':data1})

def delete(request,pk):
    print(pk)   
    data = Query.objects.get(id=pk)
    email=data.Email
    data.delete()
    data1 = Query.objects.filter(Email=email)
    data = User.objects.get(Email=email)
    fname = data.Firstname
    lname = data.Lastname
    email = data.Email
    contact = data.Contact
    password = data.Password
    user={
        'fname':fname,
        'lname':lname,
        'email':email,
        'contact':contact,
        'password':password,
    }
    return render(request,"app/home.html",{'key':user,'data':data1})

def edit(request,pk):
    data = Query.objects.get(id=pk)
    email = data.Email
    query = data.Query
    id = data.id
    data2 = {
        'email':email,
        'query':query,
        'id':id
    }  
    data = User.objects.get(Email=email)
    fname = data.Firstname
    lname = data.Lastname
    email = data.Email
    contact = data.Contact
    password = data.Password
    user={
        'fname':fname,
        'lname':lname,
        'email':email,
        'contact':contact,
        'password':password,
    }
    data1 = Query.objects.filter(Email=email)
    return render(request,"app/home.html",{'key':user,'key2':data2,'data':data1})

def update(request,pk):
    print(pk)
    email = request.POST['email']
    query = request.POST['query']
    data = Query.objects.get(id=pk)
    data.Email = email
    data.Query = query
    data.save()
    data = User.objects.get(Email=email)
    fname = data.Firstname
    lname = data.Lastname
    email = data.Email
    contact = data.Contact
    password = data.Password
    user={
        'fname':fname,
        'lname':lname,
        'email':email,
        'contact':contact,
        'password':password,
    }
    data1 = Query.objects.filter(Email=email)
    return render(request,"app/home.html",{'key':user,'data':data1})
