from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from users.models import User


class TestUserViewSet(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser1',
            password='>k?nP6B>=;[Wv64r'
        )
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.authenticate()
        self.url = '/api/v1/users/'

    def authenticate(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_get_users_list(self):
        response = self.client.get(self.url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1

    def test_get_user_detail(self):
        response = self.client.get(f'{self.url}{self.user.pk}/')
        assert response.status_code == status.HTTP_200_OK

    def test_create_user(self):
        new_user_data = {
            'username': 'testuser2',
            'email': 'ghziori125o@garageamazon.com',
            'password': 'g*S.UB?9^n$>Xm8'
        }
        response = self.client.post(self.url, new_user_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['username'] == new_user_data['username']

    def test_partial_update_user(self):
        response = self.client.patch(
            f'{self.url}{self.user.pk}/', {'username': 'new'})
        assert response.status_code == status.HTTP_200_OK

    def test_partial_update_user_not_auth(self):
        self.client.credentials()
        response = self.client.patch(
            f'{self.url}{self.user.pk}/', {'username': 'new'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_delete_user(self):
        response = self.client.delete(f'{self.url}{self.user.pk}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
