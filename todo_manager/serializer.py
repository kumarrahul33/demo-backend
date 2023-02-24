from rest_framework import serializers
from todo_manager.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title', 'completed']


    # def validate_title(self, value):
    #     if value == "":
    #         raise serializers.ValidationError("title should not be empty")
    
    

