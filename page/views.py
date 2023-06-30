from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from book_author.permissions import IsAuthorOrReadOnly
from .serializers import PageSerializer
from author.models import Author
from book.models import Book
from .models import Page

# Create your views here.
class AddPage(APIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PageSerializer

    def post(self, request, id):
        serializer = PageSerializer(data=request.data)
        if serializer.is_valid():
            author = request.user
            instance = Author.objects.get(email=author.email)
            book = Book.objects.get(id=id)
            if book.author != instance:
                return Response({"message": "You are not the author of this book"}, status=status.HTTP_401_UNAUTHORIZED)
            serializer.save(author=instance ,book=book)
            return Response({"message": "Book added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetBooksPages(APIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PageSerializer
    authentication_classes = []

    def get(self, request,slug,id):
        try:
            book = Book.objects.get(slug=slug)
        except Book.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            pages = book.pages.all()
            count = book.pages.count()
            page = pages[id]
        except Page.DoesNotExist:
            return Response({"message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
        except IndexError:
            return Response({"message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PageSerializer(page)
        return Response({"data":serializer.data,"count":count}, status=status.HTTP_200_OK)
    

class PageViews(APIView):
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PageSerializer

    def get(self, request,slug,id):
        try:
            book = Book.objects.get(slug=slug)
        except Book.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        pages = book.pages.all()
        count = book.pages.count()
        serializer = PageSerializer(pages, many=True)
        return Response({"data":serializer.data,"count":count}, status=status.HTTP_200_OK)
    
    def delete(self, request, slug, id):
        try:
            book = Book.objects.get(slug=slug)
        except Book.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            page = book.pages.all()
            page = page[id]
        except Page.DoesNotExist:
            return Response({"message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
        except IndexError:
            return Response({"message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
        page.delete()
        return Response({"message": "Page deleted successfully"}, status=status.HTTP_200_OK)
    
    def put(self, request, slug, id):
        try:
            book = Book.objects.get(slug=slug)
        except Book.DoesNotExist:
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
            page = book.pages.all()
            page = page[id]
        except Page.DoesNotExist:
            return Response({"message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
        except IndexError:
            return Response({"message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PageSerializer(page, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Page updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)