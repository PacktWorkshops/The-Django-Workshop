from django.contrib import admin

class BookrAdmin(admin.AdminSite):
    site_header = "Bookr Control Panel"
    logout_template = "admin/logout.html"

