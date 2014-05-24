from accounts.models import *
from django.contrib.auth.models import User

section = Section.objects.create(display_name = 'A')
industry = Industry.objects.get(display_name = 'B')#create(section = section, display_name = 'B')

user = User.objects.create_user(username = 'cpy', password = 'cpy')
company = user.profile.create_info(class_name = 'Company', industry = industry)
user = User.objects.create_user(username = 'test', password = 'test')
user.profile.create_info('Person',assets = 10000,company=Company.objects.get(pk=1), industry = industry)
user = User.objects.create_user(username = 'test2', password = 'test2')
user.profile.create_info('Person', assets = 10000,company=Company.objects.get(pk=1), industry = industry)