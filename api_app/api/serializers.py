from rest_framework import serializers
from api_app.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

    def validate(self, data):
        if data['task_name'] == data['task_description']:
            raise serializers.ValidationError('TaskName and TaskDescription cannot be same'
                                              )
        return data

    def validate_task_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError(
                'TaskName is too short')
        return value
