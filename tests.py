from accounts.models import *
from django.contrib.auth.models import User, Group, Permission

group,created = Group.objects.get_or_create(name = 'writer')
if not created:
	group.permissions.add(Permission.objects.get(codename = 'add_passage'))
	group.save()

section,_ = Section.objects.get_or_create(display_name = 'A')
industry,_ = Industry.objects.get_or_create(section = section, display_name = 'B')

user,_ = User.objects.get_or_create(username = 'cpy')
user.set_password('cpy')
user.save()
company = user.profile.create_info(class_name = 'Company', display_name = 'company', industry = industry)
user,_ = User.objects.get_or_create(username = 'test')
user.set_password('test')
user.save()
user.profile.create_info('Person',assets = 10000,company=Company.objects.get(pk=1), industry = industry)
user,_ = User.objects.get_or_create(username = 'test2',)
user.set_password('test')
user.save()
user.profile.create_info('Person', display_name = 'test2', assets = 10000,company=Company.objects.get(pk=1), industry = industry)

user,_ = User.objects.get_or_create(username = 'bank')
user.set_password('bank')
user.save()
bank = user.profile.create_info(class_name = 'Bank', assets = 10000)
