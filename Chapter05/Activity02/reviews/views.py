from django.shortcuts import render, get_object_or_404

from .models import Book, BookContributor


def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'reviews/book_list.html', context)


def book_detail(request, book_title):
    book = get_object_or_404(Book, title=book_title)
    author_role = BookContributor.ContributionRole.AUTHOR.value
    author_contributors = BookContributor.objects.filter(book=book, role=author_role)

    emails = [author_contributor.contributor.email for author_contributor in author_contributors]
    author_emails = ','.join(emails)

    context = {
        'book': book,
        'author_emails': author_emails
    }
    return render(request, 'reviews/book_detail.html', context)
