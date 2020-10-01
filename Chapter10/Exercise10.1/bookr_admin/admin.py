from django.contrib import admin
from django.contrib.auth.admin import User

class BookrAdmin(admin.AdminSite):
    site_header = "Bookr Control Panel"

admin_site = BookrAdmin(name='bookr_admin')
admin_site.register(User)
