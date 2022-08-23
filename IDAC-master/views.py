from django.shortcuts import redirect, render,HttpResponse
from .forms import ContactForm, RegisterForm

# Create your views here.
def index (request):
    return render(request,'index1.html')
    #return HttpResponse("This is index page")
def explore (request):
    return render(request,'Explore.html')
def about (request):
    return render(request,'about.html')
def contact (request):
    if request.method == "POST":
        print("Hi")
       
        form = ContactForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()

            return redirect("/")

        else:
            form = ContactForm()
    return render(request,'Contact.html')
def signup (request):
    return render(request,'signup.html')
def login (request):
    return redirect("/accounts/login")
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()

            return redirect("/")

        else:
            form = RegisterForm()

        return render(request, "signup.html", {"form":form})
    return render(request, "signup.html")