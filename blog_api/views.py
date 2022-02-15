from blog.models import Post,Comment
from rest_framework.permissions import SAFE_METHODS,BasePermission,IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import viewsets,generics,permissions
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .serializers import PostSerializer,CommentSerializer
# Create your views here.

class PostUserWritePermission(BasePermission):
     message = 'Editing post is restricted to the author only'

     def has_object_permission(self, request, view, obj):
         
         if request.method in SAFE_METHODS:
               return True
                  
         return obj.author == request.user  

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user   



class PostList(viewsets.ModelViewSet):
     premission_classes = [IsAuthenticated]
     serializer_class = PostSerializer 
     
     def get_object(self, queryset=None, **kwargs):
          item = self.kwargs.get('pk')
          return get_object_or_404(Post, slug=item)

         

     def get_queryset(self):
         return Post.objects.all()
   
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
























# class PostList(viewsets.ViewSet):
#      premission_classes = [IsAuthenticated]
#      queryset = Post.postobjects.all()

#      def list(self, request):
#           serializer_class = PostSerializer(self.queryset, many=True)
#           return Response(serializer_class.data)   
     
     
#      def create(self, request):
#           pass
     
#      def update(self, request):
#           pass
     
#      def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)
     
#      def update(self, request):
#           pass
     
#      def partial(self, request):
#           pass
     
#      def destroy(self, request):
#           pass
     
     
 

# class PostList(generics.ListCreateAPIView):
#      permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#      queryset = Post.postobjects.all()
#      serializer_class = PostSerializer

# class PostDetails(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

