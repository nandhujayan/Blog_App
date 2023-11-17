from rest_framework import serializers
from post.models import PostModel

class PostSerailizer(serializers.ModelSerializer):
    class Meta:
        model=PostModel
        fields=(
             'userid',
             'title',
             'message',
            
    
        )