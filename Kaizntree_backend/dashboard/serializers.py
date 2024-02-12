from rest_framework import serializers
from .models import Category, Tag, Items
from rest_framework import status


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate(self, data):
        if Category.objects.filter(category_name=data['category_name']).exists():
            raise serializers.ValidationError("Category already exists!")
        return data


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

    def validate(self, data):
        if Tag.objects.filter(category_name=data['category_name']).exists():
            raise serializers.ValidationError("Category already exists!")
        return data


class ItemsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Items
        fields = ('sku', 'item_name', 'category', 'tags', 'in_stock',
                  'available_stock', 'added_date')

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        tags_data = validated_data.pop('tags')

        cat_ref = CategorySerializer.create(
            CategorySerializer(), validated_data=category_data)

        item = Items.objects.create(category=cat_ref, **validated_data)

        for tag in tags_data:
            tag_ref = TagSerializer.create(
                TagSerializer(), validated_data=tag)
            item.tags.add(tag_ref)
        return item
