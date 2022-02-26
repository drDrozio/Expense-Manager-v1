from django.shortcuts import render
from .models import User, Expense

# Create your views here.
def home(request):
    users = User.objects.all()
    print(users)
    context = {}
    return render(request,'exp_v1/home.html',context)
