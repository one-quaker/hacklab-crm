from django.contrib import admin
from django.db import models
from django import forms
from django.contrib.postgres.fields import ArrayField
from django.utils.html import format_html

from .models import SiteConfig, UserProfile, UserAccess, DoorLog


class BaseAdmin(admin.ModelAdmin):
    input_size = 100
    area_size = 200

    formfield_overrides = {
        models.CharField: {'widget': forms.TextInput(attrs={'size': input_size})},
        models.URLField: {'widget': forms.TextInput(attrs={'size': input_size})},
        models.TextField: {'widget': forms.Textarea(attrs={'rows':32, 'cols': area_size})},
        ArrayField: {'widget': forms.Textarea(attrs={'rows':2, 'cols': area_size})},
        models.JSONField: {'widget': forms.Textarea(attrs={'rows':10, 'cols': area_size})},
    }


class UserAccessInline(admin.TabularInline):
    model = UserAccess


@admin.register(UserProfile)
class UserProfileAdmin(BaseAdmin):
    list_display = ('username', 'pk', 'door_key', 'access_info', 'full_name', 'like', 'last_update', 'created_at')
    list_filter = ('created_at', 'last_update')
    search_fields = ('door_key', 'first_name', 'last_name', 'username')
    readonly_fields = ('access_info', )

    inlines = [
        UserAccessInline,
    ]


@admin.register(UserAccess)
class UserAccessAdmin(BaseAdmin):
    list_display = ('user', 'access', 'created_at')
    list_filter = ('access', )
    search_fields = ('user__username', )


@admin.register(SiteConfig)
class SiteConfigAdmin(BaseAdmin):
    list_display = ('name', )


@admin.register(DoorLog)
class DoorLogAdmin(BaseAdmin):
    list_display = ('user', 'door_key', 'created_at')
