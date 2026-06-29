from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
        'january': 'Hello January',
        'february': 'Hello February',
        'march': 'Hello March',
        'april': 'Hello April'
        }

def index(request):
    return HttpResponse("Hello January!")

def february(request):
    return HttpResponse("Hello February!")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('Month not supported')

#  Month by number
def monthly_challenge_by_number(request, month):
    try:
        str_month = list(monthly_challenges.keys())[month]
        HttpResponseRedirect('/challenges/' + str_month)
        #  return HttpResponse(str_month)
    except:
        return HttpResponseNotFound('Month not supported')
