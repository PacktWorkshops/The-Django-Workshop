import csv
import re

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from reviews.models import Publisher, Contributor, Book, BookContributor, Review


class Command(BaseCommand):
    help = 'Load the reviews data from a CSV file.'

    def add_arguments(self, parser):
        parser.add_argument('--csv', type=str)

    def row_to_dict(self, row, header):
        if len(row) < len(header):
            row += [''] * (len(header) - len(row))
        return dict([(header[i], row[i]) for i, head in enumerate(header) if head])

    def handle(self, *args, **options):
        m = re.compile('content:(\w+)')
        header = None
        models = dict()
        try:
            with open(options['csv']) as csvfile:
                model_data = csv.reader(csvfile)
                for i, row in enumerate(model_data):
                    if max([len(cell.strip()) for cell in row[1:] + ['']]) == 0 and m.match(row[0]):
                        model_name = m.match(row[0]).groups()[0]
                        models[model_name] = []
                        header = None
                        continue
 
                    if header is None:
                        header = row
                        continue

                    row_dict = self.row_to_dict(row, header)
                    if set(row_dict.values()) == set(['']):
                        continue
                    models[model_name].append(row_dict)

        except FileNotFoundError as f:
                raise CommandError('File "%s" does not exist' % options['csv'])

        for data_dict in models.get('Publisher', []):
            print('Publisher')
            p = Publisher(name=data_dict['publisher_name'],
                          website=data_dict['publisher_website'],
                          email=data_dict['publisher_email'])
            p.save()

        for data_dict in models.get('Book', []):
            print('Book')
            b = Book(title=data_dict['book_title'],
                     publication_date=data_dict['book_publication_date'].replace('/', '-'),
                     isbn=data_dict['book_isbn'],
                     publisher=Publisher.objects.filter(name=data_dict['book_publisher_name']).first())
            b.save()

        for data_dict in models.get('Contributor', []):
            print('Contributor')
            c = Contributor(first_names=data_dict['contributor_first_names'],
                            last_names=data_dict['contributor_last_names'],
                            email=data_dict['contributor_email'])
            c.save()

        for data_dict in models.get('BookContributor', []):
            print('BookContributor')
            bc = BookContributor(book=Book.objects.filter(title=data_dict['book_contributor_book']).first(),
                                 contributor=Contributor.objects.filter(email=data_dict['book_contributor_contributor']).first(),
                                 role=data_dict['book_contributor_role'])
            bc.save()

        for data_dict in models.get('Review', []):
            print('Review')
            review = Review(content=data_dict['review_content'], rating=data_dict['review_rating'],
                        date_created=data_dict['review_date_created'],
                        date_edited=data_dict['review_date_edited'],
                        creator=User.objects.get(email=data_dict['review_creator']),
                        book=Book.objects.filter(title=data_dict['review_book']).first())
            review.save()
