from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


User = get_user_model()


try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass


@admin.register(User)
class LinguaFlowUserAdmin(UserAdmin):
    list_display = ("id", "username", "email", "is_staff", "is_superuser", "is_active", "date_joined")
    list_display_links = ("id", "username")
    list_filter = ("is_staff", "is_superuser", "is_active", "date_joined")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("-date_joined",)
