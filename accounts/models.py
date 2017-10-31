from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    USER_TYPE_CHOICE = (
    	('materialplanning', 'materialplanning'),
    	('productdevelopment', 'productdevelopment'),
    	('production', 'production'),
    	('admin', 'admin')
    )
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICE, default='admin')
    description = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)

    def __str__(self):
    	return "username:" + self.user.username + "     pk:" + str(self.pk)

def create_profile(sender, **kwargs):
	if kwargs['created']: #true
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)