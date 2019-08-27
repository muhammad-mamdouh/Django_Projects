from rest_framework import generics
from postings.models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostAPIView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
