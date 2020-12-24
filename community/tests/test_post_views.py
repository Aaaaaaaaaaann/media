from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from users.models import User


class TestPostVewSet(APITestCase):
    fixtures = ['user.json', 'post.json']

    def setUp(self):
        self.user = User.objects.get(pk=2)
        self.client = APIClient()
        self.authenticate()
        self.url = '/api/v1/posts/'

    def authenticate(self):
        self.client.force_authenticate(user=self.user)

    def test_get_posts_list_no_auth(self):
        self.client.credentials()
        response = self.client.get(self.url)
        assert response.status_code == status.HTTP_200_OK

    def test_create_post(self):
        post_data = {
            'author': self.user.pk,
            'title': 'Tittle',
            'content': 'Content.'
        }
        response = self.client.post(self.url, post_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == post_data['title']

    def test_create_post_as_another_user(self):
        post_data = {
            # We are user 2.
            'author': 3,
            'title': 'Tittle',
            'content': 'Content.'
        }
        response = self.client.post(self.url, post_data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_create_post_no_data(self):
        post_data = {
            'author': None,
            'title': None,
            'content': None
        }
        response = self.client.post(self.url, post_data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_partial_update_post(self):
        new_data = {'content': 'Changed content.'}
        response = self.client.patch(f'{self.url}1/', new_data)
        assert response.status_code == status.HTTP_200_OK

    def test_delete_post(self):
        response = self.client.delete(f'{self.url}1/')
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_delete_post_of_another_user(self):
        another_user = User.objects.create_user(
            username='testuser2',
            password='>k?nP6B>=;[Wv64r'
        )
        with open('/home/anna/output.txt', 'w') as file:
            file.write(str(another_user.pk))
        self.client.force_authenticate(user=another_user)
        response = self.client.delete(f'{self.url}1/')
        assert response.status_code == status.HTTP_403_FORBIDDEN


class TestUserPost(APITestCase):
    fixtures = ['user.json', 'post.json']

    def setUp(self):
        self.client = APIClient()
        self.url = '/api/v1/users/2/posts/'

    def test_get_users_posts(self):
        response = self.client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
