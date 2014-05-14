from accounts.models import *
from django.contrib.auth.models import User

user = User.objects.create_user(username = 'test2', password = 'test')
user.profile.info = Person.objects.create(assets = 10000)
user.profile.save()
user = User.objects.create_user(username = 'cpy2', password = 'cpy')
user.profile.info = Company.objects.create()
user.profile.save()