import re
from rest_framework import serializers

from stuapp.models import *


class ActorSerializer(serializers.Serializer):
    """演员序列化"""

    GENDER_ID = (
        ('0', '男'),
        ('1', '女')
    )

    aid = serializers.IntegerField(label='编号',read_only=True)
    aname = serializers.CharField(label='年龄',max_length=30)
    age = serializers.IntegerField(label='年龄', required=False)
    agender = serializers.ChoiceField(choices=GENDER_ID, label='性别', required=False)
    birth_date = serializers.DateField(label='出生年月', required=False)
    photo = serializers.ImageField(label='头像', required=False)

    def validate(self, attrs):
        print(attrs)

        aname = attrs['aname']
        age = attrs['age']

        if 'hello' in aname:
            raise serializers.ValidationError("aname 字段值不能包含hello")

        reg = r'^[123]\d{1}$'
        v = str(age)
        if not re.match(reg, v):
            raise serializers.ValidationError("age 字段值必须在10-40之间")

        return attrs

    def create(self, validated_data):
        """新建"""
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        instance.aname = validated_data.get('aname',instance.aname)
        instance.age = validated_data.get('age',instance.age)
        instance.agender = validated_data.get('agender', instance.agender)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.photo = validated_data.get('photo', instance.photo)

        instance.save()
        return instance


class MovieSerializer(serializers.Serializer):
    mid = serializers.IntegerField(label='影片编号',read_only=True)
    mname = serializers.CharField(label='影片名称',max_length=30)
    m_pub_date = serializers.DateField(label='上映日期',required=False)
    mread = serializers.IntegerField(label='阅读量')
    mcomment = serializers.CharField(label='评论',max_length=300,required=False,allow_null=True)
    mimage = serializers.ImageField(label='图片',required=False)
    # actors = serializers.PrimaryKeyRelatedField(label='演员',read_only=True)
    # actors = ActorSerializer()
    actor = serializers.StringRelatedField(label='演员')

