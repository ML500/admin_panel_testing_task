import pytest

from django.urls import reverse

from users.models import CustomUser
from api.models import Category, Article


@pytest.mark.django_db
def test_categories_list_view(client):
    url = reverse('categories_list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_articles_list_view(client):
    url = reverse('articles_list')
    response = client.get(url)
    assert response.status_code == 200


# @pytest.mark.django_db
# def test_users_list_view(client):
#     url = reverse('users_list')
#     response = client.get(url)
#     assert response.status_code == 200

@pytest.mark.django_db
def test_users_detail_view(client):
    user = CustomUser.objects.create_user(username='test_name')
    url = reverse('user_detail', kwargs={'id': user.user_id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_categories_detail_view(client):
    category = Category.objects.create(category_name='test_category')
    url = reverse('category_detail', kwargs={'id': category.category_id})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_articles_detail_view(client):
    article = Article.objects.create(article_name='article_test', article_image='/default_image')
    url = reverse('article_detail', kwargs={'id': article.article_id})
    response = client.get(url)
    assert response.status_code == 200

