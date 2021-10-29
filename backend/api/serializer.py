from rest_framework import serializers
from users.models import CustomUser
from api.models import Category, Article


class BaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'category_name']


class CategorySerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(read_only=True)
    category_parent = BaseCategorySerializer()

    class Meta:
        model = Category
        fields = ['category_id', 'category_name', 'category_parent']


class CategorySerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'category_name', 'category_parent']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['user_id', 'username']


class BaseArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['article_id', 'category', 'user', 'article_name', 'article_description', 'article_image']


class ArticleSerializerGet(serializers.ModelSerializer):
    category = BaseCategorySerializer(read_only=True)
    user = UserSerializerBase(read_only=True, )

    class Meta:
        model = Article
        fields = '__all__'


class ArticleSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
