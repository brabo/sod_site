# Create your views here.
from django.shortcuts import render

from sod.models import Stats

def index(request):
    return render(request, 'index')

def stats(request):
#    head = "SOD basic stats"
#    dns = "DNS servers found            : "
    dns = str(Stats.objects.all().count())
#    dnsopen = "Open DNS servers found     : "
    dnsopen = str(Stats.objects.filter(open=1, size__gt=25).count())
#    dnsrec = "Recursive DNS servers found : "
    dnsrec = str(Stats.objects.filter(open=1, recursive=1, size__gt=25).count())

#    template = loader.get_template('sod/templates/stats/index.html')
    context = {
#        'head' : head,
        'dns' : dns,
        'dnsopen' : dnsopen,
        'dnsrec' : dnsrec,
    }

    return render(request, 'stats/stats', context)

from sod.models import Query
from sod.forms import Countries
from django.db import connection

from django.http import HttpResponseRedirect

def query(request):
#    countries = Query.objects.raw('SELECT DISTINCT country from ips')
#    cursor = connection.cursor()
#    cursor.execute("SELECT DISTINCT country from ips")
#    countries = cursor.fetchall()
#    countries = Query.objects.all().distinct()
#    countries = Query.objects.only("country").distinct()
    countries = Query.objects.values('country').distinct()
    context = {
        'countries' : countries,
    }
    return render(request, 'query/query', context)

