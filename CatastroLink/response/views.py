from django.shortcuts import render
from django.http import HttpResponse
from .models import DisasterReport, User
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point


def check_disaster_threshold(request):
    disaster_reports = DisasterReport.objects.values('latitude', 'longitude').annotate(report_count=Count('id')).filter(report_count__gte=5)
    
    for report in disaster_reports:
        disaster_location = Point(report['longitude'], report['latitude'])
        nearby_users = User.objects.filter(latitude__isnull=False, longitude__isnull=False)
        
        for user in nearby_users:
            user_location = Point(user.longitude, user.latitude)
            distance = disaster_location.distance(user_location)  
            
            if distance <= D(km=25):
                prompt_user_role(user)

    return HttpResponse("Disaster check complete.")

def select_role(request, user_id):
    user = User.objects.get(id=user_id)
    
    if request.method == 'POST':
        role = request.POST.get('role')
        if role in ['client', 'host']:
            user.role = role
            user.save()
            return HttpResponse(f"{user.username}'s role has been updated to {role}.")
    
    return render(request, 'select_role.html', {'user': user})