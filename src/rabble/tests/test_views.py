import pytest
from django.urls import reverse
from rabble.models import subRabble, Community, Post, Comment
from .factories import UserFactory, CommunityFactory, SubRabbleFactory, PostFactory, CommentFactory

@pytest.mark.django_db
def test_index_view(client):
    community = CommunityFactory(community_identifier="default")

    for _ in range(5):
        SubRabbleFactory(community_id=community)
    assert subRabble.objects.count() == 5

    response = client.get(reverse("index"))
    assert response.status_code == 200

    assert len(response.context["subrabbles"]) == 5

@pytest.mark.django_db
def test_subrabble_detail_view(client):
    sub_rabble = SubRabbleFactory()

    for _ in range(5):
        post = PostFactory(subRabble_id=sub_rabble)
        CommentFactory(post_id=post)

    assert Post.objects.count() == 5
    assert Comment.objects.count() == 5

    response = client.get(reverse("subrabble-detail", args=[sub_rabble.identifier]))
    assert response.status_code == 200

    assert len(response.context["posts"]) == 5
    for post in response.context["posts"]:
        assert post.comments.count() >= 1

@pytest.mark.django_db
def test_post_create_view(client):
    user = UserFactory()
    client.force_login(user)

    sub_rabble = SubRabbleFactory()

    post_data = {
        "title": "Test Post",
        "body": "This is a test.",
        "privacy": False,
        "anonymous": False,
        "subRabble_id": sub_rabble.id,
    }
    response = client.post(reverse("post-create", args=[sub_rabble.identifier]), post_data)

    assert response.status_code == 302

    assert Post.objects.count() == 1
    db_post = Post.objects.get(title="Test Post")
    assert db_post.body == "This is a test."
    assert db_post.account_id == user
    assert db_post.subRabble_id == sub_rabble