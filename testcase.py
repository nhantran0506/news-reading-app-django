from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from apps.users.models import User
from apps.roles.enums import Roles
from django.core import mail
from apps.followers.models import Follower
from apps.articles.models import Article
from apps.category.enums import Category
from apps.comments.models import Comment

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from apps.users.models import User

class UserViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.existing_user_data = {
            'username': 'existinguser@example.com',
            'first_name': 'Existing',
            'last_name': 'User',
            'role': Roles.Author.value,
            'password': 'testpassword123'
        }
        self.user = User.objects.create_user(**self.existing_user_data)

        self.new_user_data = {
            'username': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User',
            'role': Roles.Author.value,
            'password': 'testpassword123'
        }

    def test_create_user(self):
        response = self.client.post('/api/users/', self.new_user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(username='newuser@example.com').username, 'newuser@example.com')


    def test_get_user(self):
        response = self.client.get(f'/api/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)

    def test_update_user(self):
        update_data = {'first_name': 'Updated'}
        response = self.client.patch(f'/api/users/{self.user.id}/', update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Updated')

    def test_delete_user(self):
        response = self.client.delete(f'/api/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)

    def test_forgot_password(self):
        response = self.client.post(reverse('forgot-password'), {'username': self.user.username})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(username=self.user.username)
        self.assertIsNotNone(user.reset_code)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [self.user.username])
        self.assertIn('Your password reset code is', mail.outbox[0].body)

    def test_reset_password(self):
        self.client.post(reverse('forgot-password'), {'username': self.user.username})
        user = User.objects.get(username=self.user.username)
        response = self.client.post(reverse('reset-password'), {'username': user.username, 'reset_code': user.reset_code, 'new_password': 'newpassword'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(User.objects.get(username=self.user.username).check_password('newpassword'))



# Followers
class FollowerTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1_data = {
            'username': 'user1@example.com',
            'password': 'password1',
            'first_name': 'User',
            'last_name': 'One',
            'role': Roles.Author.value,
        }
        self.user1 = User.objects.create_user(**self.user1_data)

        self.user2_data = {
            'username': 'user2@example.com',
            'password': 'password2',
            'first_name': 'User',
            'last_name': 'Two',
            'role': Roles.Author.value,
        }
        self.user2 = User.objects.create_user(**self.user2_data)

    def test_create_follower(self):
        follower_data = {
            'user': self.user1.pk,
            'follower': self.user2.pk,
        }
        response = self.client.post(reverse('core_api:follower-list'), follower_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Follower.objects.count(), 1)
        self.assertEqual(Follower.objects.get(user=self.user1).follower, self.user2)

    def test_get_follower(self):
        follower = Follower.objects.create(user=self.user1, follower=self.user2)
        response = self.client.get(reverse('core_api:follower-detail', kwargs={'pk': follower.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['follower']['id'], self.user2.pk)


    def test_delete_follower(self):
        follower = Follower.objects.create(user=self.user1, follower=self.user2)
        response = self.client.delete(reverse('core_api:follower-detail', kwargs={'pk': follower.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Follower.objects.count(), 0)



# Articles 
class ArticleTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'user1@example.com',
            'password': 'password1',
            'first_name': 'User',
            'last_name': 'One',
            'role': Roles.Publisher.value,
        }
        self.user = User.objects.create_user(**self.user_data)
        self.article_data = {
            'title': 'Test Article',
            'content': 'This is a test article.',
            'user': self.user,
            'category': Category.EDUCATION.value,
    
        }

    def test_create_article(self):
        response = self.client.post('/api/articles/', self.article_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(Article.objects.get(title='Test Article').user, self.user)


    def test_get_article(self):
        article = Article.objects.create(**self.article_data)
        response = self.client.get(reverse('core_api:articles-detail', kwargs={'pk': article.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], article.title)

    def test_update_article(self):
        article = Article.objects.create(**self.article_data)
        new_data = {'title': 'Updated Title'}
        response = self.client.patch(reverse('core_api:articles-detail', kwargs={'pk': article.pk}), new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Article.objects.get(pk=article.pk).title, 'Updated Title')

    def test_delete_article(self):
        article = Article.objects.create(**self.article_data)
        response = self.client.delete(reverse('core_api:articles-detail', kwargs={'pk': article.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Article.objects.count(), 0)


# Comment
class CommentTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'user1@example.com',
            'password': 'password1',
            'first_name': 'User',
            'last_name': 'One',
            'role': Roles.Author.value,
        }
        self.user = User.objects.create_user(**self.user_data)
        self.article_data = {
            'title': 'Test Article',
            'content': 'This is a test article.',
            'user': self.user,
            'category': Category.EDUCATION.value,
        }
        self.article = Article.objects.create(**self.article_data)
        self.comment_data = {
            'content': 'This is a test comment.',
            'user': self.user,
            'article': self.article,
        }

    def test_create_comment(self):
        response = self.client.post('/api/comments/', self.comment_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.get(content='This is a test comment.').user, self.user)

    def test_get_comment(self):
        comment = Comment.objects.create(**self.comment_data)
        response = self.client.get(reverse('core_api:comments-detail', kwargs={'pk': comment.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], comment.content)

    def test_update_comment(self):
        comment = Comment.objects.create(**self.comment_data)
        new_data = {'content': 'Updated comment.'}
        response = self.client.patch(reverse('core_api:comments-detail', kwargs={'pk': comment.pk}), new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.get(pk=comment.pk).content, 'Updated comment.')

    def test_delete_comment(self):
        comment = Comment.objects.create(**self.comment_data)
        response = self.client.delete(reverse('core_api:comments-detail', kwargs={'pk': comment.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comment.objects.count(), 0)


# Login
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import User

class LoginTestCase(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'user1@example.com',
            'password': 'password1',
            'first_name': 'User',
            'last_name': 'One',
            'role': Roles.Author.value,
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_login_success(self):
        response = self.client.post(reverse('login'), {'username': 'user1@example.com', 'password': 'password1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('refresh' in response.data)
        self.assertTrue('access' in response.data)

    def test_login_fail_wrong_password(self):
        response = self.client.post(reverse('login'), {'username': 'user1@example.com', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error'], 'Invalid username or password')

    def test_login_fail_no_username(self):
        response = self.client.post(reverse('login'), {'password': 'password1'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
