from django.contrib import admin

class BookrAdminSite(admin.AdminSite):
    index_title = 'Bookr site admin'
    title_header = 'Bookr Admin'
    site_header = 'Bookr administration'
