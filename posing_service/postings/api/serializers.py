from rest_framework import serializers
from postings.models import BlogPost


# Converts to JSON and
# Validations for data passed
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        read_only_fields = ['user']
        # fields = [
        #     'pk',
        #     'user',
        #     'title',
        #     'content',
        #     'timestamp',
        # ]

    def validate_title(self, value):
        qs = BlogPost.objects.filter(title__iexact=value)
        # Exclude the current retrieved instance
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError('This title has already been used')
        return value
