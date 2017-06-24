from django.shortcuts import render, redirect
from random
import datetime
from _future_ import unicode_literals

def index(request):
        try:
            request.session['gold']
        except KeyError:
            request.session['gold']=0
        try:
            reques.session['activities']
        except KeyError:
