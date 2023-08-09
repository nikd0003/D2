(venv) PS C:\!Course\SF_D\D2\NewsPaper>
# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell 
>>> from news.models import *
>>> user1 = User.objects.create(username='First', first_name='Nik')
>>> Author.objects.create(authorUser=user1)
>>> user2 = User.objects.create(username='Second', first_name='Egor')
>>> Author.objects.create(authorUser=user2)
>>> Category.objects.create(name='Technology')
>>> Category.objects.create(name='Education')
>>> Category.objects.create(name='Society')
>>> Category.objects.create(name='NewsFeed')
>>> Category.objects.create(name='Sport')
>>> Category.objects.create(name='Culture')
>>> Category.objects.create(name='Politics')
>>> Category.objects.create(name='Opinions')
>>> Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='First')), categoryType='NW', title='First title', text='First text text text text')
>>> Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='First')), categoryType='AR', title='Second title', text='Second text text text text')
>>> Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Second')), categoryType='NW', title='First2 title', text='First2 text text text text')
>>> Post.objects.create(author=Author.objects.get(authorUser=User.objects.get(username='Second')), categoryType='AR', title='Second2 title', text='Second2 text text text text')
>>> p1 = Post.objects.get(pk=1)
>>> p2 = Post.objects.get(pk=2)
>>> p3 = Post.objects.get(pk=3)
>>> p4 = Post.objects.get(pk=4)
>>> c1 = Category.objects.get(name='Technology')
>>> c2 = Category.objects.get(name='Education')
>>> c3 = Category.objects.get(name='Different')
>>> c4 = Category.objects.get(name='New')
>>> p1.postCategory.add(c1)
>>> p2.postCategory.add(c1, c2, c3, c4)
>>> p3.postCategory.add(c3, c2)
>>> p4.postCategory.add(c4)
>>> Comment.objects.create(commentUser=User.objects.get(username='First'), commentPost = Post.objects.get(pk=1), text='comment text1')
>>> Comment.objects.create(commentUser=User.objects.get(username='Second'), commentPost = Post.objects.get(pk=1), text='comment text2')
>>> Comment.objects.create(commentUser=User.objects.get(username='First'), commentPost = Post.objects.get(pk=2), text='comment text1')
>>> Comment.objects.create(commentUser=User.objects.get(username='Second'), commentPost = Post.objects.get(pk=3), text='comment text1')
>>> Comment.objects.create(commentUser=User.objects.get(username='Second'), commentPost = Post.objects.get(pk=4), text='comment text1')
>>> Post.objects.get(pk=1).like()
>>> Post.objects.get(pk=1).like()
>>> Post.objects.get(pk=1).like()
>>> Post.objects.get(pk=1).like()
>>> Post.objects.get(pk=2).like()
>>> Post.objects.get(pk=2).like()
>>> Post.objects.get(pk=2).like()
>>> Post.objects.get(pk=2).like()
>>> Post.objects.get(pk=3).like()
>>> Post.objects.get(pk=3).like()
>>> Post.objects.get(pk=4).dislike()
>>> Post.objects.get(pk=2).dislike()
>>> Post.objects.get(pk=1).dislike()
>>> Comment.objects.get(pk=1).like()
>>> Comment.objects.get(pk=1).like()
>>> Comment.objects.get(pk=1).dislike()
>>> Comment.objects.get(pk=2).like()
>>> Comment.objects.get(pk=2).like()
>>> Comment.objects.get(pk=2).like()
>>> Comment.objects.get(pk=2).dislike()
>>> Comment.objects.get(pk=3).like()
>>> Author.objects.get(authorUser = User.objects.get(username="First")).update_rating()
>>> Author.objects.get(authorUser = User.objects.get(username="Second")).update_rating()
# a = Author.objects.get(authorUser = User.objects.get(username="First"))
# b = Author.objects.get(authorUser = User.objects.get(username="Second"))
# a.ratingAuthor
# b.ratingAuthor
# Author.objects.get(authorUser = User.objects.get(username="First")).ratingAuthor
# best = Author.objects.all().order_by('-ratingAuthor').values('authorUser', 'ratingAuthor') [0]
# print(best)
