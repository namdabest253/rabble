from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rabble.models import *
from .serializers import UserSerializer, subRabbleSerializer, PostSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request' : request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def subRabble_list(request):
    if request.method == 'GET':
        subRabbles = subRabble.objects.all()
        serializer = subRabbleSerializer(subRabbles, many=True, context={'request' : request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = subRabbleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def post_list(request, identifier):
    if request.method == 'GET':
        subrabble = subRabble.objects.get(identifier=identifier)
        posts = Post.objects.filter(subRabble_id=subrabble)
        serializer = PostSerializer(posts, many=True, context={'request' : request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'POST', 'PATCH', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
    status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
    status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'POST', 'PATCH', 'DELETE'])
def subRabble_detail(request, identifier):
    try:
        subrabble = subRabble.objects.get(identifier=identifier)
    except subRabble.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = subRabbleSerializer(subrabble)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = subRabbleSerializer(subrabble, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
    status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = subRabbleSerializer(subrabble, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
    status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        subrabble.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'POST', 'PATCH', 'DELETE'])
def post_detail(request, identifier, pk):
    try:
        subrabble = subRabble.objects.get(identifier=identifier)
        post = Post.objects.get(pk=pk, subRabble_id=subrabble)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user_has_liked = False
    if request.user.is_authenticated:
        user_has_liked = PostLike.objects.filter(post=post, user=request.user).exists()

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
    status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
    status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    serializer = PostSerializer(post)
    return Response({
        "post": serializer.data,
        "subrabble": subrabble.identifier,
        "user_has_liked": user_has_liked
    })

@api_view(['POST', 'GET'])  # Allow GET so we can override its response
def toggle_like(request, identifier, pk):
    if request.method == 'GET':
        return Response({
            "usage": {
                "user": "user1"
            },
            "description":{
                "liked": True,
                "like_count": 12
            }
        })

    username = request.data.get("user")
    if not username:
        return Response({"error": "User is required"}, status=400)

    try:
        user = User.objects.get(username=username)
        subrabble = subRabble.objects.get(identifier=identifier)
        post = Post.objects.get(pk=pk, subRabble_id=subrabble)
    except (User.DoesNotExist, subRabble.DoesNotExist, Post.DoesNotExist):
        return Response(status=404)

    like, created = PostLike.objects.get_or_create(user=user, post=post)

    if not created:
        like.delete()
        liked = False
    else:
        liked = True

    like_count = post.likes.count()
    return Response({"liked": liked, "like_count": like_count})

