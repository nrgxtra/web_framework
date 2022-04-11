from rest_framework import serializers

from books_rest.books_api.models import Book


class BookSerializer(serializers.ModelSerializer):
    def validate(self, data):
        title = data.get('title')[0]
        if not title.isupper():
            raise serializers.ValidationError('title must start with uppercase letter!')
        return data

    class Meta:
        model = Book
        # fields = '__all__'
        exclude = ('id',)
