from django.db import models
from django.db.models import Sum
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, post_delete
from django.contrib.postgres.fields import ArrayField
from django.conf import settings


class CreatedMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class EnabledManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(enabled=True)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class UserProfile(CreatedMixin):
    first_name = models.CharField(max_length=256, blank=True, null=True)
    last_name = models.CharField(max_length=256, blank=True, null=True)
    username = models.CharField(max_length=256, unique=True) # Slack username
    door_key = models.CharField(max_length=16, unique=True)
    access_info = ArrayField(
            models.CharField(max_length=16, blank=True),
            size=32,
            blank=True,
            default=list,
    )

    like = models.PositiveIntegerField(blank=True, default=0)
    last_update = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.username if self.username else self.first_name

    @property
    def full_name(self):
        if self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.first_name


class UserAccess(CreatedMixin):
    ACC_DOOR = 'door'
    ACC_CNC= 'cnc'
    ACC_BIGCNC = 'bigcnc'
    ACC_LATHE = 'lathe'
    ACC_LASER = 'laser'
    ACC_BANDSAW = 'bandsaw'
    ACC_MILL = 'mill'
    ACC_CHOICES = (
        (ACC_DOOR, ACC_DOOR),
        (ACC_CNC, ACC_CNC),
        (ACC_BIGCNC, ACC_BIGCNC),
        (ACC_LATHE, ACC_LATHE),
        (ACC_LASER, ACC_LASER),
        (ACC_BANDSAW, ACC_BANDSAW),
        (ACC_MILL, ACC_MILL),
    )

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='access_list')
    access = models.CharField(max_length=16, choices=ACC_CHOICES)

    class Meta:
        unique_together = [['user', 'access']]

    def __str__(self):
        return f'{self.user} - {self.access}'


class DoorLog(CreatedMixin):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True, related_name='door_log')
    door_key = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self):
        return f'{self.user} {self.door_key}'


class SiteConfig(models.Model):
    name = models.CharField(max_length=128)
    logo = models.FileField(upload_to='conf')

    def __str__(self):
        return self.name


@receiver(post_delete, sender=UserAccess)
@receiver(post_save, sender=UserAccess)
def update_access_info(sender, instance, **kwargs):
    user = UserProfile.objects.get(pk=instance.user.pk)
    user.access_info = [x.access for x in UserAccess.objects.filter(user__pk=user.pk)]
    user.save()
