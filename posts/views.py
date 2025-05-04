from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Post
from .serializer import PostSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import status

# Register View(user)
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message":"User crated successfully"},
            status = status.HTTP_201_CREATED,
            headers = headers
        )

# List and Create(post) view
class PostListCreateview(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self,serializer):
        serializer.save(author=self.request.user)

# Retrieve, Update, or Destroy view(post)   
class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_permissions(self):
        if self.request.method in ['PUT','DELETE']:
            return[permissions.IsAuthenticated()]
        return super().get_permissions()
    
    def get_object(self):
        obj = super().get_object()
        if self.request.method in ['PUT','DELETE'] and obj.author != self.request.user:
            raise permissions.PermissionDenied("Sorry you do not have permission to perform this action.")
        return obj
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Post deleted successfully."}, status=status.HTTP_200_OK)