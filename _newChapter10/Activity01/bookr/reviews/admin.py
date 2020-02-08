from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review, ReviewerProfile


class PublisherAdmin(admin.ModelAdmin):
    search_fields = ('name__startswith',)

class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn', 'publisher__name')

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    list_filter = ('last_names',)
    search_fields = ('last_names__startswith', 'first_names')

# Register your models here.
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)
