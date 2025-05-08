import pytest
from django.urls import reverse
from rabble.models import Post
from rabble.tests.factories import (
    UserFactory, SubRabbleFactory, PostFactory
)

from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_subrabble_get(api_client):
    subrabble = SubRabbleFactory()

    url = f"/api/subRabbles/!{subrabble.identifier}/"
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["identifier"] == subrabble.identifier
    assert response.json()["title"] == subrabble.title


@pytest.mark.django_db
def test_post_post(api_client):
    user = UserFactory()
    subrabble = SubRabbleFactory()

    api_client.force_authenticate(user=user)

    url = f"/api/subRabbles/!{subrabble.identifier}/posts/"
    data = {
        "title": "New API Post",
        "body": "Body from API",
        "privacy": False,
        "anonymous": False,
    }

    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

    post = Post.objects.get(pk=response.data["id"])
    assert post.title == data["title"]
    assert post.body == data["body"]
    assert post.subRabble_id == subrabble
    assert post.account_id == user


@pytest.mark.django_db
def test_post_patch(api_client):
    post = PostFactory(title="Old Title")
    url = f"/api/subRabbles/!{post.subRabble_id.identifier}/posts/{post.pk}/"

    api_client.force_authenticate(user=post.account_id)

    patch_data = {"title": "Updated Title"}
    response = api_client.patch(url, patch_data)

    assert response.status_code == status.HTTP_200_OK

    post.refresh_from_db()
    assert post.title == "Updated Title"
