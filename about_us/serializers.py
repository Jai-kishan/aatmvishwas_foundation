from rest_framework import serializers
from about_us.models import AboutUs, TeamMember

# class AboutUsSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     description = serializers.CharField(max_length=250)
#     image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url="/media")

#     def create (self, validate_data):
#         return AboutUs.objects.create(**validate_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.image = validated_data.get('image', instance.image)
#         instance.save()
#         return instance


class AboutUsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['id', 'title', 'description', 'image']