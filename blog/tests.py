from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category

class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='Django')
        
        testuser1 = User.objects.create_user(
            username='test_user_1',
            password = 'qazwsx678'
        )

        test_post = Post.objects.create(
            category_id = 1,
            title = 'Post Title',
            excerpt = 'Post excerpt',
            content = 'Post content',
            slug = 'Post slug',
            author_id = 1,
            status = 'published'
        )

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        
        self.assertEqual(author, 'test_user_1')
        self.assertEqual(excerpt, 'Post excerpt')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(content, 'Post content')
        self.assertEqual(status, 'published')

        self.assertEqual(str(post), 'Post Title')
        self.assertEqual(str(cat), 'Django')