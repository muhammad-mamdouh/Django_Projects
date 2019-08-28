from rest_framework import serializers
from postings.models import BlogPost


# Converts to JSON and
# Validations for data passed
class BlogPostSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = BlogPost
        # fields = '__all__'
        fields = [
            'uri',
            'pk',
            'user',
            'title',
            'content',
            'timestamp',
        ]
        read_only_fields = ['user']

    def get_uri(self, object):
        request = self.context.get('request')
        return object.get_api_url(request=request)

    def validate_title(self, value):
        qs = BlogPost.objects.filter(title__iexact=value)
        # Exclude the current retrieved instance
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError('This title has already been used')
        return value
