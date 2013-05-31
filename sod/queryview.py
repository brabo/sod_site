from sod.models import Query
from sod.forms import Countries

from django.http import HttpResponseRedirect

def index(request):
    countries = str(Query.objects.raw('SELECT DISTINCT country from ips'))
    context = {
        'countries' : countries,
    }
    return render(request, 'query/index.html', context)


