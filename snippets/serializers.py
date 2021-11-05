#from typing_extensions import required
from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

# class SnippetSerializer(serializers.Serializer):
#     """직렬화/역직렬화 field 정의"""
# 값 검증을 위한 옵션 추가 가능
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    # code = serializers.CharField(style={'base_template':'textarea.html'})
    # linenos = serializers.BooleanField(required=False)
    # language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    # style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
# serialize가 호출됐을 때
    def create(self, validated_data):
        """검증한 데이터로 새 'Snippet' 인스턴스를 생성하여 반환"""
        return Snippet.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """검증한 데이터로 기존 'Snippet' 인스턴스를 업데이트한 후 반환"""
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
    
    