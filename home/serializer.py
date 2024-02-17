from rest_framework import serializers
from .models import Todo
import re
from django.template.defaultfilters import slugify

class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    class Meta:
        model = Todo
        fields = '__all__'
        # fields = ['todo_title','uid','slug']
        # exclude = ['created_at','updated_at']

    # The slugify filter returns a text into one long word containing nothing but lower case ASCII characters and hyphens (-).
    def get_slug(self, obj):
        
        # return slugify(obj.todo_title)
        return 'NoorulNisa'     # we can return anything in slug
    
    # >>>>>> to validate single field, data will contain only todo_title
    def validate_todo_title(self, data):
        if data:
            print(data)
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:}]')
            if len(data) < 5:
                print('length error')
                raise serializers.ValidationError('Title must be more than 10 characters')
            if not (regex.search(data) == None):
                print('special character symbol')
                raise serializers.ValidationError('Todo tile can not contain special characters')
        return data
    
    # >>>>> here validate_data will contain all fields
    # def validate(self, validate_data):
    #     if validate_data.get('todo_title'):
    #         todo_title = validate_data['todo_title']
    #         regex = re.compile('[@_!#$%^&*()<>?/\|}{~:}]')

    #         if len(todo_title) < 10:
    #             raise serializers.ValidationError('Title must be more than 10 characters')
    #         if not (regex.search(todo_title) == None):
    #             raise serializers.ValidationError('Todo tile can not contain special characters')
            
    #     return validate_data
