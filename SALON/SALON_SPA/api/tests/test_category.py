import pytest
from rest_framework import status


@pytest.fixture
def create_category(api_client):
    def do_create_category(category):
        return api_client.post('/api/categories/', category)
    return do_create_category


@pytest.mark.django_db
class TestCreateCategory():
    def test_is_user_not_admin_return_403(self, create_category, authenticate_user):
        authenticate_user(is_staff=False)

        response = create_category({'category': 'Shoes'})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_is_data_invalid_return_400(self, create_category, authenticate_user):
        
        response = create_category({'category': ''})

        assert response.data is not None


@pytest.mark.django_db
class TestListCategory():
    def test_is_admin_return_200(self, authenticate_user, api_client):
        authenticate_user()

        response = api_client.get('/api/categories/', {'category': 'Shoes'})

        assert response.status_code == status.HTTP_200_OK
