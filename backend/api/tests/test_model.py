import pytest
from users.models import CustomUser
from api.models import Article, Category


@pytest.mark.django_db
def test_user_create():
    CustomUser.objects.create_user('john', 'password')
    assert CustomUser.objects.count() == 1


@pytest.mark.django_db
def test_article_create():
    category = Category.objects.create(category_name='category_1', )
    user = CustomUser.objects.create_user('john', 'password')
    Article.objects.create(category=category, user=user, article_name='tests', article_description='test_test',
                           article_image='/default')
    assert Article.objects.count() == 1

@pytest.mark.django_db
def test_category_create():
    category = Category.objects.create(category_name='parent_test')
    Category.objects.create(category_name='tests', category_parent=category)
    assert Category.objects.count() == 2
