from rest_framework import generics, mixins
from postings.models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostAPIView(mixins.CreateModelMixin , generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # Add the POST HTTP Verb to the view
    # This post method is handled by the upper mixin
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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
