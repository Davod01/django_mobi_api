from rest_framework import serializers
from .models import mobile
# from .models import Colors

# class mobileSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     title = serializers.CharField(max_length=255)
#     price = serializers.IntegerField()
#     slug = serializers.SlugField()
#     display = serializers.CharField(max_length=100,null=True, required=False)
#     display_size = serializers.CharField(100, null=True)
#     resolution = serializers.CharField(100, null=True)
#     os = serializers.CharField(100, null=True)
#     Weight = serializers.IntegerField(null=True)
#     batery = serializers.CharField(max_length=30, null=True)
#     colors = serializers.ChoiceField(choices=Colors.choices,default=Colors.black)
#     Introduction = serializers.TextField(null=True, blank=True)
#     expert_check = serializers.TextField(null=True, blank=True)
#     created = serializers.DateTimeField(auto_now=True)
#     updated = serializers.DateField(null=True, blank=True)

class mobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = mobile
        fields = '__all__'
        lookup_field = 'slug'