from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from users.models import CustomUser
from api.models import Category, Article
from api.serializer import CategorySerializer, CategorySerializerPost, UserSerializer, ArticleSerializerGet, \
    ArticleSerializerPOST


@csrf_exempt
def categoryApi(request, id=0):
    if request.method == 'GET':
        categories = Category.objects.all()
        categories_serializer = CategorySerializer(categories, many=True)
        return JsonResponse(categories_serializer.data, safe=False)
    elif request.method == 'POST':
        category_data = JSONParser().parse(request)
        categories_serializer = CategorySerializerPost(data=category_data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method == 'PUT':
        category_data = JSONParser().parse(request)
        category = Category.objects.get(category_id=category_data['category_id'])
        categories_serializer = CategorySerializerPost(category, data=category_data)
        if categories_serializer.is_valid():
            categories_serializer.save()
            return JsonResponse('Update Successfully', safe=False)
        return JsonResponse('Failed Update')
    elif request.method == 'DELETE':
        category = Category.objects.get(category_id=id)
        category.delete()
        return JsonResponse('Delete successfully', safe=False)


@csrf_exempt
def userApi(request, id=0):
    if request.method == 'GET':
        users = CustomUser.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        print(user_data)
        user = CustomUser.objects.get(user_id=user_data['user_id'])
        users_serializer = UserSerializer(user, data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse('Update Successfully', safe=False)
        return JsonResponse('Failed Update')
    elif request.method == 'DELETE':
        user = CustomUser.objects.get(user_id=id)
        user.delete()
        return JsonResponse('Delete successfully', safe=False)


@csrf_exempt
def articleApi(request, id=0):
    if request.method == 'GET':
        articles = Article.objects.all()
        articles_serializer = ArticleSerializerGet(articles, many=True)
        return JsonResponse(articles_serializer.data, safe=False)
    elif request.method == 'POST':
        article_data = JSONParser().parse(request)
        articles_serializer = ArticleSerializerPOST(data=article_data)
        if articles_serializer.is_valid():
            articles_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse('Failed to Add', safe=False)
    elif request.method == 'PUT':
        article_data = JSONParser().parse(request)
        article = Article.objects.get(article_id=article_data['article_id'])
        articles_serializer = ArticleSerializerPOST(article, data=article_data)
        if articles_serializer.is_valid():
            articles_serializer.save()
            return JsonResponse('Update Successfully', safe=False)
        return JsonResponse('Failed Update')
    elif request.method == 'DELETE':
        article = Article.objects.get(article_id=id)
        article.delete()
        return JsonResponse('Delete successfully', safe=False)


@csrf_exempt
def save_file(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
