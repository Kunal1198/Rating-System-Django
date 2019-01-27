from django.shortcuts import *
from django.http import *
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions	import ObjectDoesNotExist
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status



User = get_user_model() 


def index(request):
	if request.method=="POST":
		username = request.POST['user']
		password = request.POST['pas']
		try:
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				auth.login(request,user)
				return redirect('/polls/')
			else:
				messages.error(request,'Username and Password incorrect')

		except auth.ObjectNotExist:
			print("Invalid User")
	return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        form1 =studreg(request.POST or None)
        if form1.is_valid():
            new_user = form1.save(commit=False)
            new_user.set_password(form1.cleaned_data['password'])
            new_user.save()
            #messages.success(request,'user is registered')
            #student.objects.create(created=new_user)
            return redirect('/polls/login/')
    else:
        form1 = studreg()
    context = {
        'form1': form1,
    }
    return render(request, 'register.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_profile = UserEditForm(data=request.POST or None, instance=request.user)
        #profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)
        if user_profile.is_valid():
            user_profile.save()
            return redirect('/polls/')
    else:
        user_profile = UserEditForm(instance=request.user)
        #profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'user_profile': user_profile,
        #'profile_form': profile_form,
    }
    return render(request, 'edit_profile.html', context)


def user_logout(request):
    logout(request)
    return redirect('/polls/login/')

def landing(request):
    return render(request,'landing.html')
 
@login_required
def proctor(request):
    if request.method == 'POST':
        form = UserProctorForm(request.POST, request.FILES)
        #user_profile = UserEditForm(data=request.POST or None, instance=request.user)
        if form.is_valid():
            new_user=form.save(commit=False)
            new_user.created=request.user
            new_user.save()
            return redirect('/polls/')
    else:
        form = UserProctorForm()
        #user_profile = UserEditForm(instance=request.user)
    context = {
        'form': form,
        #'user_profile':user_profile,
    }
    return render(request, 'student.html', context)


@login_required
def edit_form(request):
    if request.method == 'POST':
        user_form = EditProctorForm(data=request.POST or None, instance=request.user.student)
        if user_form.is_valid():
            user_form.save()
            return redirect('/polls/')
            
    else:
        user_form = EditProctorForm(instance=request.user.student)

    context = {
        'user_form': user_form,
    }
    return render(request, 'edit_form.html', context)

def hel(request):
        return render(request, 'charts.html')

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    #model = student

    def get(self, request, format=None):
        qs1 = student.objects.filter(question1='E1').count()
        qs2 = student.objects.filter(question1='G1').count()
        qs3 = student.objects.filter(question1='A1').count()
        qs4 = student.objects.filter(question1='P1').count()
        qa1 = student.objects.filter(question='E').count()
        qa2 = student.objects.filter(question='G').count()
        qa3 = student.objects.filter(question='A').count()
        qa4 = student.objects.filter(question='P').count()
        qb1 = student.objects.filter(question2='E2').count()
        qb2 = student.objects.filter(question2='G2').count()
        qb3 = student.objects.filter(question2='A2').count()
        qb4 = student.objects.filter(question2='P2').count()
        qc1 = student.objects.filter(question3='E3').count()
        qc2 = student.objects.filter(question3='G3').count()
        qc3 = student.objects.filter(question3='A3').count()
        qc4 = student.objects.filter(question3='P3').count()
        #serializer = Page1Serializer(qs_count, many=True)
        labels = ["Visa", "Master Card", "Paypal","Hii"]
        default_items = [qs1, qs2, qs3, qs4]
        labels1 = ["Excellent", "Good", "Average", "Poor"]
        default_items1 = [qa1, qa2, qa3, qa4]
        labels2 = ["Visa", "Master Card", "Paypal","Hii"]
        default_items2 = [qb1, qb2, qb3, qb4]
        labels3 = ["Excellent", "Good", "Average", "Poor"]
        default_items3 = [qc1, qc2, qc3, qc4]
        data = {
                "labels": labels,
                "default": default_items,
                "labels1": labels1,
                "default1": default_items1,
                "labels2": labels2,
                "default2": default_items2,
                "labels3": labels3,
                "default3": default_items3,
        }
        
        return Response(data)
  