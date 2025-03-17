from rest_framework.views import APIView
from rest_framework.response import Response
from sesna.apps.books.models import Book
from rest_framework import status

from sesna.apps.books.serializers import BookSerializer
from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class PingView(APIView):
    def get(self, request):
        all_books = Book.objects.all().values()
        response = {
            'books': list(all_books),
            'status_code': 200
        }
        return Response(response, status=status.HTTP_200_OK)


class BooksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get all books
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        response = {
            'books': serializer.data,
            'status_code': 200
        }
        return Response(response, status=status.HTTP_200_OK)

        # # Paginate the data with 10 items per page
        # paginator = PageNumberPagination()
        # paginator.page_size = 10
        # paginated_books = paginator.paginate_queryset(books, request)

        # # Serialize the data
        # serializer = BookSerializer(paginated_books, many=True)
        # response = {
        #     'books': serializer.data,
        #     'status_code': 200
        # }
        # return paginator.get_paginated_response(response)
    

class TokenObtainPairView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            response = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'status_code': 200
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'error': 'Invalid credentials',
                'status_code': 401
            }
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)
