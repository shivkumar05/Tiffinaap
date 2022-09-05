from time import tzname
from django.shortcuts import redirect, render
from django.utils import timezone
import zoneinfo




class TimezoneMiddleware:
   def __init__(self, get_response):
        self.get_response = get_response

   def __call__(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(zoneinfo.ZoneInfo(tzname))
        else:
            timezone.deactivate()
        return self.get_response(request)


# Prepare a map of common locations to timezone choices you wish to offer.
common_timezones = {
    'London': 'Europe/London',
    'Paris': 'Europe/Paris',
    'New York': 'America/New_York',
}

def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return render(request, 'time.html', {'timezones': common_timezones})
        #return redirect('/')
    else:
        return render(request, 'time.html', {'timezones': common_timezones})
