from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
        'january': 'Hello January',
        'february': 'Hello February',
        'march': 'Hello March',
        'april': 'Hello April'
        }

def index(request):
    return HttpResponse("Hello index!")

def february(request):
    return HttpResponse("Hello February!")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(f'<h1>{challenge_text}</h1>')
    except:
        return HttpResponseNotFound('Month not supported')

#  Month by number
def monthly_challenge_by_number(request, month):
    # Starting from 1.
    month = month - 1
    if month > 12 or month < 1:
        return HttpResponseNotFound('Month not supported')
    try:
        str_month = list(monthly_challenges.keys())[month]
        return HttpResponseRedirect(reverse('month-challenge', args=[str_month]))
        #  return HttpResponseRedirect('/challenges/' + str_month)
    except:
        return HttpResponseNotFound('Month not supported')
