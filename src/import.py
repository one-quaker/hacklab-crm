import os, sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_app.settings')
import django
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F, Q
from django.forms.models import model_to_dict
from django.utils import timezone
from django.core.files import File

django.setup()
from prismo.models import UserProfile, UserAccess


data = None
with open('dump.sql') as f:
    data = f.read()


UserProfile.objects.all().delete()
for i in data.split('\n'):
    # print(f'processing: {i}')
    user_id, name, door_key, door, cnc, lathe, bigcnc, laser, bandsaw, mill = [None for x in range(10)]
    try:
        user_id, name, door_key, door, cnc, lathe, bigcnc, laser, bandsaw, mill = i.split('\t')
    except:
        print(i)

    user_qs = UserProfile.objects.filter(username=name)
    if user_qs:
        print(f'skip user "{user_id}: {name}"\n{i}\n==================')
        continue

    try:
        user = UserProfile()
        user.username = name
        user.door_key = door_key
        user.save()

        if door == '1':
            user_acc = UserAccess(user=user, access=UserAccess.ACC_DOOR)
            user_acc.save()

        if cnc == '1':
            user_acc = UserAccess(user=user, access=UserAccess.ACC_CNC)
            user_acc.save()

        if lathe == '1':
            user_acc = UserAccess(user=user, access=UserAccess.ACC_LATHE)
            user_acc.save()

        if bigcnc == '1':
            user_acc = UserAccess(user=user, access=UserAccess.ACC_BIGCNC)
            user_acc.save()

        if laser == '1':
            user_acc = UserAccess(user=user, access=UserAccess.ACC_LASER)
            user_acc.save()

        if bandsaw == '1':
            user_acc = UserAccess(user=user, access=UserAccess.ACC_BANDSAW)
            user_acc.save()

        if mill == '1':
            user_acc = UserAccess(user=user, access=UserAccess.ACC_MILL)
            user_acc.save()
    except:
        print(i)
