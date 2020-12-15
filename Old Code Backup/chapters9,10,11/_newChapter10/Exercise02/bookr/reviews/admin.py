from django.contrib import admin
from django.utils.html import format_html
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

class ReviewerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'has_profile_photo')
    list_editable= ('location',)

    # def _get_thumbnail(self, obj):
    #      return '<img src="%s" />' % obj.admin_thumbnail.url
    def has_profile_photo(self, obj):
        return obj.profile_photo and format_html('<h1>&#128511;</h1>')  or ''

# Register your models here.
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)
admin.site.register(ReviewerProfile, ReviewerProfileAdmin)
