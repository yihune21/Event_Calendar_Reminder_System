from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReminderSerializer
from pymongo import MongoClient

# Initialize MongoDB client
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['reminder_db']  # Ensure the correct database name
collection = db['reminders']  # Ensure the correct collection name

class ReminderAPIView(APIView):
    def post(self, request):
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            collection.insert_one(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        reminders = list(collection.find())
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data)