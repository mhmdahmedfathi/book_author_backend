from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from book_author.permissions import IsAuthorOrReadOnly
from .serializers import BookSerializer
from author.models import Author
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Book

# Create your views here.
class AddBook(APIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = BookSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        print(request.data)
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            author = request.user
            instance = Author.objects.get(email=author.email)
            serializer.save(author=instance)
            return Response({"message": "Book added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BookViews(APIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = BookSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_authenticators(self):
        if self.request.method == 'GET':
            return []
        return super(BookViews, self).get_authenticators()
    
    def put(self, request, id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Book updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        try:
            author = Author.objects.get(email=request.user.email)
            book = Book.objects.get(id=id, author=author)
        except Book.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response({"message": "Book deleted successfully"}, status=status.HTTP_200_OK)
    
class DeleteBook(APIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = BookSerializer

    def delete(self, request, slug):
        try:
            book = Book.objects.get(slug=slug)
        except Book.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        book.delete()
        return Response({"message": "Book deleted successfully"}, status=status.HTTP_200_OK)


class GetBooks(APIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = BookSerializer
    authentication_classes = []

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
class GetAuthorBooks(APIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = BookSerializer

    def get(self, request):
        try:
            author = Author.objects.get(email=request.user.email)
        except Author.DoesNotExist:
            return Response({"message": "Author not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            books = Book.objects.filter(author=author)
        except Book.DoesNotExist:
            return Response({"message": "Books not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)