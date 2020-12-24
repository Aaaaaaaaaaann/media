from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from users.models import User


class TestPostVewSet(APITestCase):
    fixtures = ['user.json', 'post.json', 'comment.json']

    def setUp(self):
        self.user = User.objects.get(pk=2)
        self.client = APIClient()
        self.authenticate()
        self.url = '/api/v1/posts/1/comments/'

    def authenticate(self):
        self.client.force_authenticate(user=self.user)

    def test_get_single_comment(self):
        response = self.client.get(f'{self.url}1/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['author'] == self.user.pk

    def test_create_comment(self):
        comment_data = {
            'author': self.user.pk,
            'post': 1,
            'parent': 1,
            'content': 'Another comment.'
        }
        response = self.client.post(self.url, comment_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['content'] == comment_data['content']

    def test_create_comment_as_another_user(self):
        comment_data = {
            # We are user 2.
            'author': 3,
            'post': 1,
            'parent': 1,
            'content': 'Another comment.'
        }
        response = self.client.post(self.url, comment_data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_partial_update_comment(self):
        new_data = {'content': 'New content'}
        response = self.client.patch(f'{self.url}1/', new_data)
        assert response.status_code == status.HTTP_200_OK

    def test_partial_update_comment_of_another_user(self):
        another_user = User.objects.create_user(
            username='testuser2',
            password='>k?nP6B>=;[Wv64r'
        )
        self.client.force_authenticate(user=another_user)
        new_data = {'content': 'New content'}
        response = self.client.patch(f'{self.url}1/', new_data)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_comment(self):
        response = self.client.delete(f'{self.url}1/')
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_delete_comment_no_auth(self):
        self.client.force_authenticate()
        response = self.client.delete(f'{self.url}1/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
