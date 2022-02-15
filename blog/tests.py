from typing import ParamSpecKwargs
from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


# Create your tests here.
class Ters_Create_Post(TestCase):

    @classmethod
    def setUpClass(cls):
        test_category = Category.objects.create(mame='django')
        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789'
        )
        test_post = Post.objects.create(
            category_id =1, title='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=1, status='published'
        )
    
    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        contetn = f'{post.content}'
        status = f'{post.status}'

         