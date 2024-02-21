from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# class UserModelAdmin(BaseUserAdmin):
#   # The fields to be used in displaying the User model.
#   # These override the definitions on the base UserModelAdmin
#   # that reference specific fields on auth.User.
#   model = User
#   list_display = ('id', 'name', 'email', 'date_of_birth','phone_number','bloodgroup','province_number','address','issue', 'is_admin')
#   list_filter = ('is_admin',)
#   fieldsets = (
#       ('User Credentials', {'fields': ('phone_number', 'password')}),
#       ('Personal info', {'fields': ('name', 'email', 'date_of_birth','bloodgroup','province_number','address','issue')}),
#       ('Permissions', {'fields': ('is_admin',)}),
#   )
#   # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
#   # overrides get_fieldsets to use this attribute when creating a user.
#   add_fieldsets = (
#       (None, {
#           'classes': ('wide',),
#           'fields': ('name', 'email', 'date_of_birth','phone_number','bloodgroup','province_number','address','issue','password'),
#       }),
#   )
#   search_fields = ('phone_number',)
#   ordering = ('phone_number', 'id')
#   filter_horizontal = ()


# Now register the new UserModelAdmin...
admin.site.register(User)