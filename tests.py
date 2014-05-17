from accounts.models import *
from django.contrib.auth.models import User

user = User.objects.create_user(username = 'cpy', password = 'cpy')
user.profile.info = Company.objects.create()
user.profile.save()
user = User.objects.create_user(username = 'test', password = 'test')
user.profile.info = Person.objects.create(assets = 10000,company=Company.objects.get(pk=1))
user.profile.save()
user = User.objects.create_user(username = 'test2', password = 'test2')
user.profile.info = Person.objects.create(assets = 10000,company=Company.objects.get(pk=1))
user.profile.save()