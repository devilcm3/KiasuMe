# Create your views here.
from django.shortcuts import render
from store.models import *
import os

def index(request):
	context = {
	'home':'active'
	}
	return render(request,'store/index.html',context)