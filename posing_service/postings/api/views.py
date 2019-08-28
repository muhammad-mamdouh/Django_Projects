from django.db.models import Q
from rest_framework import generics, mixins
from postings.models import BlogPost
from .permissions import IsOwnerOrReadOnly
from .serializers import BlogPostSerializer


class BlogPostAPIView(mixins.CreateModelMixin , generics.ListAPIView):
    serializer_class   = BlogPostSerializer
    permission_classes = [IsOwnerOrReadOnly]   # Also you can add any permission classes right here

    def get_queryset(self):
        queryset = BlogPost.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            queryset = queryset.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # Add the POST HTTP Verb to the view
    # This post method is handled by the upper mixin
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}


class BlogPostRUDView(generics.RetrieveUpdateDestroyAPIView):
    # What field inside of our model are we looking up for?
    lookup_field = 'pk'    # Default value is the pk
    queryset = BlogPost.objects.all()

    # If you want to overwrite the queryset method
    # def get_queryset(self):
    #     return BlogPost.objects.all()

    # If you want to overwrite the get specific object method
    # def get_object(self):
    #     pk = self.kwargs.get('pk')
    #     return BlogPost.objects.get(pk=pk).filter(......)

    serializer_class = BlogPostSerializer

    def get_serializer_context(self, *args, **kwargs):
        return {'request': self.request}
