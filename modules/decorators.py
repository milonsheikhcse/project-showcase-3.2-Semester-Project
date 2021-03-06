from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User

def not_in_group(*group_names):
    def in_groups(user):
        if user.is_authenticated:
            if bool(user.groups.filter(name__in=group_names)):
                return False
        return True
    return user_passes_test(in_groups, login_url='product:index')

def group_required(*group_names):
    def in_groups(user):
        if user.is_authenticated:
            if bool(user.groups.filter(name__in=group_names)) | user.is_superuser:
                return True
        return False
    return user_passes_test(in_groups, login_url='product:index')