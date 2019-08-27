from rest_framework import serializers
from postings.models import BlogPost


# Converts to JSON and
# Validations for data passed
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

        # fields = [
        #     'pk',
        #     'user',
        #     'title',
        #     'content',
        #     'timestamp',
        # ]
