from django.contrib.auth.models import Group, Permission

nivel_1 = Group.objects.create(name='Nível 1')
nivel_2 = Group.objects.create(name='Nível 2')
nivel_3 = Group.objects.create(name='Nível 3')


nivel_1.permissions.add(Permission.objects.get(codename='view_product'))
nivel_2.permissions.add(Permission.objects.get(codename='change_product'))
nivel_3.permissions.add(Permission.objects.get(codename='manage_product'))