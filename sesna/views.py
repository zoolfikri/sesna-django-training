from rest_framework.views import APIView
from rest_framework.response import Response
from sesna.apps.books.models import Book
from rest_framework import status

class PingView(APIView):
    def get(self, request):
        all_books = Book.objects.all().values()
        response = {
            'books': list(all_books),
            'status_code': 200
        }
        return Response(response, status=status.HTTP_200_OK)


class BooksView(APIView):
    def get(self, request):
        title = request.query_params.get('title', None)
        books = Book.objects.filter(title=title).values()
        response = {
            'books': books,
            'status_code': 200
        }
        return Response(response, status=status.HTTP_200_OK)
