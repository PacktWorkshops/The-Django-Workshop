from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review

class PublisherAdmin(admin.ModelAdmin):
    search_fields = ('name__startswith',)


class ContributorInline(admin.TabularInline):
    model = BookContributor
    extra = 0

class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn', 'publisher__name')

    
    inlines = (ContributorInline,)

    # inlines = (admin.StackedInline('ContributorBook', admin.site),)
    # 'parent_model' and 'admin_site'  # 'contributors',)


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    list_filter = ('last_names',)
    search_fields = ('last_names__startswith', 'first_names')


class BookContributorAdmin(admin.ModelAdmin):
    role = {'rating': admin.HORIZONTAL}


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('creator', 'book', 'rating')
    list_max_show_all = 20
    list_per_page = 10
    radio_fields = {'rating': admin.HORIZONTAL}

    list_filter = ('content', 'creator__username', 'book__title')
    search_fields = ('creator__username',)
    show_full_result_count = False
    preserve_filters = False
    def get_readonly_fields(self, request, obj=None):
        if obj is None or request.user.is_superuser:
            return self.readonly_fields
        return ['creator', 'book',] + self.readonly_fields


# Register your models here.
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor, BookContributorAdmin)
admin.site.register(Review, ReviewAdmin)
