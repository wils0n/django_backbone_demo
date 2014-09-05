from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from .models import Entry


class EntryResource(ModelResource):
    
    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'

class UserResource(ModelResource):
		
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']