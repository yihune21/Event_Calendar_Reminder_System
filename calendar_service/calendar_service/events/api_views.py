import threading
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .mongodb import MongoDBClient
from .serializers import EventSerializer
from datetime import datetime
from bson.objectid import ObjectId
from .producer import EventProducer
from .consumer import Consumer

producer = EventProducer()
consumer = Consumer()
threading.Thread(target=consumer.start_consuming).start()

mongo_client = MongoDBClient()
collection = mongo_client.get_collection("events")

class EventList(APIView):
    def get(self, request):
        events = list(collection.find({}))
        
        # Format the events data
        formatted_events = []
        for event in events:
            formatted_event = {
                "id": str(event.get("_id")),
                "title": event.get("title"),
                "start": event.get("start_date"),
                "end": event.get("end_date"),
                "description": event.get("description"),
                "category": event.get("category"),
                "user_id": str(event.get("user_id")),  # Convert ObjectId to string for response
            }
            
            # Parse and reformat the dates
            try:
                if formatted_event["start"]:
                    formatted_event["start"] = self.parse_date(formatted_event["start"])
                if formatted_event["end"]:
                    formatted_event["end"] = self.parse_date(formatted_event["end"])
            except ValueError as e:
                # Log the error if parsing fails
                print(f"Error parsing date: {e}")
                continue
            
            formatted_events.append(formatted_event)
        
        return Response(formatted_events, status=status.HTTP_200_OK)

    @staticmethod
    def parse_date(date_str):
        """Parses a date string and returns an ISO 8601 formatted string."""
        formats = [
            "%Y-%m-%dT%H:%M:%SZ",  # ISO format with 'Z'
            "%Y-%m-%d %H:%M:%S",   # Common format with space
        ]
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt).isoformat()
            except ValueError:
                continue
        raise ValueError(f"Date format not recognized: {date_str}")
    
    def post(self, request):
        data = request.data.copy()
        user_id = consumer.get_latest_message()
        if user_id is None:
            return Response({"error": "No user ID received"}, status=status.HTTP_400_BAD_REQUEST)
        data['user_id'] = user_id
        print("##########", data['user_id'], "##########")

        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.create(serializer.validated_data)
            collection.insert_one(validated_data)
            producer.publish_event(validated_data.get("title"))
            # producer.publish_event(validated_data.get("start_date").isoformat())  # Convert datetime to string
            # producer.publish_event(validated_data.get("end_date").isoformat())    # Convert datetime to string
            # producer.publish_event(validated_data.get("description"))
            # producer.publish_event(validated_data.get("category"))
            producer.publish_event(str(validated_data.get("_id")))  # Publish _id as string
            # producer.publish_event(str(validated_data.get("user_id")))  # Publish user_id as string
            producer.close_connection()
            return Response({"message": "Event created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetail(APIView):
    
    def post(self, request):
        # Convert id to ObjectId
        event_id = request.data.get("id")
        try:
            event_id = ObjectId(event_id)
        except Exception as e:
            return Response({"error": "Invalid event ID format"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            result = collection.update_one({"_id": event_id}, {"$set": serializer.data})
            if result.matched_count:
                return Response({"message": "Event updated successfully"}, status=status.HTTP_200_OK)
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        # Convert id to ObjectId  
        event_id = request.query_params.get("id")     
        try:
            event_id = ObjectId(event_id)
        except Exception as e:
            return Response({"error": "Invalid event ID format"}, status=status.HTTP_400_BAD_REQUEST)

        result = collection.delete_one({"_id": event_id})
        
        if result.deleted_count:
            return Response({"message": "Event deleted successfully"}, status=status.HTTP_200_OK)
        return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

class LatestMessage(APIView):
    def get(self, request):
        message = consumer.get_latest_message()
        if message:
            return Response({"message": message}, status=status.HTTP_200_OK)
        return Response({"error": "No message received"}, status=status.HTTP_404_NOT_FOUND)