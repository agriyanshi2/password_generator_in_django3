from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
	return render(request, 'generator/home.html')


def password(request):
	thepassword=" "
	char=list('abcdefghijklmnopqrstuvwxyz')
	
	if request.GET.get('uc'):
		char.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
	
	if request.GET.get('no'):
		char.extend(list("0123456789"))
	
	if request.GET.get('sc'):
		char.extend(list("!@#$%^&*()_+={}:',.<>/"))
	
	len=int(request.GET.get('length',12))
	
	for x in range(len):
		thepassword+= random.choice(char)
		
	return render(request,'generator/password.html', {'password':thepassword})
