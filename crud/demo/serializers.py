from django.core.exceptions import ValidationError
from rest_framework import serializers

from demo.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    text = serializers.CharField(min_length=10)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']

    def validate_text(self, value):
        if 'text' in value:
            raise ValidationError('недопустимое слово')
        return value

    # def validate(self, attrs):
    #     if 'hello' in attrs['text'] or attrs['user'].id == 2:
    #         raise ValidationError
    #     return attrs

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)



