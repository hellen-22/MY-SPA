import pytest
from rest_framework.test import APIClient

from customuser.models import CustomUser

@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticate_user(api_client):
    def do_authenticate(is_staff=True):
        return api_client.force_authenticate(user=CustomUser(is_staff=is_staff))
    return do_authenticate