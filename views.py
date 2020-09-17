from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import travel

# Create your views here.
def index(request):
   return render(request,'index.html')


def discover(request):  
   if request.method=='POST':
     checkin=request.POST['checkin-date']
     checkout=request.POST['checkout-date']
     room=request.POST['room']
     adult=request.POST['adults']
     children= request.POST['children']

     messages.success(request,'Your room is booked....')
     return redirect(discover)
   else:
      return render(request,'index.html')


def contact(request):

  t=travel()
  t.contact='+917709931941'
  t.email='nihaarmahajan5@gmail.com'
  t.address='Raisoni Nagar,Jalgaon'
  
  return render(request,'contact.html',{'t':t})


def about(request):
  return render(request,'about.html')  
   

def room(request):
  if request.method=='POST':
     checkin=request.POST['checkInDate']
     checkout=request.POST['checkOutDate']
     adult=request.POST['adults']
     children= request.POST['children']

     messages.success(request,'Your room is booked....')
     return redirect(room)
  else:
      return render(request,'room.html')  