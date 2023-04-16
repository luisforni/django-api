from rest_framework import serializers
from .models import Product, Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['title', 'description', 'grade']

class ProductSerializer(serializers.ModelSerializer):
    average_rating = serializers.DecimalField(max_digits=3, decimal_places=1, read_only=True)
    total_reviews = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'average_rating', 'total_reviews']

    def create(self, validated_data):
        reviews_data = validated_data.pop('reviews', [])
        product = Product.objects.create(**validated_data)
        for review_data in reviews_data:
            Review.objects.create(product=product, **review_data)
        return product
