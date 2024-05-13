from django.shortcuts import render

# Create your views here.
from rest_framework import status
from api_app.api.serializers import TodoSerializer
from rest_framework.decorators import api_view
from api_app.models import Todo
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'api_app/index.html')


@api_view(['GET', 'POST'])
def todo_list(request):
    print(request.method, "------------")
    print(request.headers)
    print("=============================***********")
    if request.method == 'GET':
        todo_list = Todo.objects.filter(active=True).order_by('created_at')
        serializer = TodoSerializer(todo_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = {}
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['msg'] = "Successfully created"
            data['result'] = serializer.data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    print(request.method, "------------")
    print(request.headers)
    print("=============================***********")
    try:
        todo = Todo.objects.get(pk=pk)
    except:
        return Response({"error": "No data found for given id"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        todo.delete()
        return Response({"Message": "Data Deleted"}, status=status.HTTP_204_NO_CONTENT)
