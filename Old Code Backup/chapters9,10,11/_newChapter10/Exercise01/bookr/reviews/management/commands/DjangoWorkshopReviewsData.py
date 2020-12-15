import datetime
import random
import csv
import sys

book_titles = [
'Advanced Deep Learning with Keras',
'Hands-On Machine Learning for Algorithmic Trading',
'Architects of Intelligence',
'Deep Reinforcement Learning Hands-On',
'Natural Language Processing with TensorFlow',
'Hands-On Reinforcement Learning with Python',
'Brave New World',
'The Grapes of Wrath',
'For Whom The Bell Tolls',
'To Kill A Mocking Bird',
'The Great Gatsby',
'The Catcher in the Rye',
'Farenheit 451',
'Pride and Prejudice',
'1984',
'Animal Farm: A Fairy Story',
'Paul Clifford',
'The Talisman',
]


users = ['alice', 'bob', 'carol', 'david']


review_content_rating = [
    ('Fascinating work.', 5),
    ('Great Read.', 5),
    ('Inspiring.', 5),
    ('I can''t put this one down..', 5),
    ('Interesting book.', 4),
    ('Quite good.', 4),
    ('Fair.', 3),
    ('Interesting.', 3),
    ('Definitely just for the fans.', 2),
    ('A tad mediocre.', 2),
    ('Not my cup of tea.', 1),
    ]


csvfile = sys.stdout

csvwriter = csv.writer(csvfile)  # , delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

header = ['review_content', 'review_rating', 'review_date_created', 'review_date_edited', 'review_creator', 'review_book']
csvwriter.writerow(header)

for user in users:
    time_now = datetime.datetime.now() - datetime.timedelta(days=60) 
    for book_title in book_titles:
        if random.random()<0.5:
            continue
        review_content, review_rating = random.choice(review_content_rating)
        time_now += datetime.timedelta(days=random.randint(0, 10)) + datetime.timedelta(seconds=int(random.random()*24*3600))   
        review_date_created = time_now.strftime('%Y-%m-%d %H:%M:%S')
        review_date_edited = (time_now + datetime.timedelta(seconds=int(random.random()*24*3600))).strftime('%Y-%m-%d %H:%M:%S')
        csvwriter.writerow([review_content, review_rating, review_date_created, review_date_edited, user, book_title])

"""
content:Review,,,,,
review_content,review_rating,review_date_created,review_date_edited,review_creator,review_book
A must read for all,5,2020-01-04 16:31:40.376237,2020-01-04 16:31:40.376237,peterjones@test.com,Advanced Deep Learning with Keras
An ok read,3,2020-01-04 16:31:40.376237,2020-01-04 16:31:40.376237,marksandler@test.com,Advanced Deep Learning with Keras
"""
