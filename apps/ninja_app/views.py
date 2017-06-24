# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
import datetime
from django.shortcuts import render, redirect #, HttpResponse

# Create your views here.
def index(request):
    # print "Don't waste the rest of your time here worrying about other people."
    # print '- Marcus Aurelius'
    try:
        request.session['gold']
    except KeyError:
        request.session['gold'] = 0
    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []
    return render(request, 'ninja_app/index.html')

def process_money(request):
    if request.method == 'POST':
        if request.POST['place'] == 'farm':
            this_gold = random.randrange(10, 21)
            request.session['gold'] += this_gold
            request.session['activities'].append(
                'Earned ' + str(this_gold) + ' gold from the farm! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
        elif request.POST['place'] == 'cave':
            this_gold = random.randrange(5, 11)
            request.session['gold'] += this_gold
            request.session['activities'].append(
                'Earned ' + str(this_gold) + ' gold from the cave! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
        elif request.POST['place'] == 'house':
            this_gold = random.randrange(2, 6)
            request.session['gold'] += this_gold
            request.session['activities'].append(
                'Earned ' + str(this_gold) + ' gold from the house! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
        elif request.POST['place'] == 'casino':
            this_gold = random.randrange(-50, 51)
            if this_gold > 0:
                request.session['activities'].append(
                    'Won ' + str(this_gold) + ' gold from the casino! (' +
                    '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
                )
            elif this_gold < 0:
                if (this_gold * -1) > request.session['gold']:
                    this_gold = request.session['gold'] * -1
                request.session['activities'].append(
                    'Lost ' + str(this_gold) + ' gold at the casino...' +
                    'ouch. ({:%Y/%m/%d %I:%M %p})'.format(
                        datetime.datetime.now()
                    )
                )
            elif this_gold == 0:
                request.session['activities'].append(
                    "Went to the casino and broke even...can't be lucky " +
                    "every time! " +
                    '({:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
                )
            request.session['gold'] += this_gold
    return redirect('/')
