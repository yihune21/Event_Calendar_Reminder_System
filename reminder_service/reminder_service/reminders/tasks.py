# from celery import shared_task
# from .models import Reminder
# from django.utils.timezone import now
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
# import os

# @shared_task
# def send_reminders():
#     reminders = Reminder.objects.filter(reminder_time__lte=now(), is_sent=False)
#     for reminder in reminders:
#         try:
#             send_email(reminder.user.email, reminder.message)
#             print(f"Sending reminder: {reminder.message}")
#             reminder.is_sent = True
#             reminder.save()
#         except Exception as e:
#             print(f"Failed to send reminder: {reminder.message}. Error: {e}")

# def send_email(user_email, message):
#     email = Mail(
#         from_email='your_email@example.com',
#         to_emails=user_email,
#         subject='Reminder Notification',
#         plain_text_content=message,
#     )
#     sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
#     sg.send(email)


from celery import shared_task
from .models import Reminder
from django.utils.timezone import now
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import timedelta
import os

# MongoDB connection
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['reminders']
events_collection = db['events']

@shared_task
def send_reminders():
    # Calculate the time 1 minute from now
    one_minute_from_now = now() + timedelta(minutes=1)
    
    # Fetch events starting in 1 minute
    events = events_collection.find({"start_date": one_minute_from_now})
    
    for event in events:
        try:
            user_id = event.get("user_id")
            user_email = get_user_email(user_id)
            if user_email:
                send_email(user_email, f"Reminder: Your event '{event.get('title')}' is starting soon.")
                print(f"Sending reminder for event: {event.get('title')} to {user_email}")
            else:
                print(f"User email not found for user_id: {user_id}")
        except Exception as e:
            print(f"Failed to send reminder for event: {event.get('title')}. Error: {e}")


def get_user_email(user_id):
    users_collection = db['users']
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        return user.get("email")
    return None

def send_email(to_email, message):
    sg = SendGridAPIClient(os.getenv('gTpfyWJG7grFqYcV0VGrvNtP8tlBiWJy'))
    email = Mail(
        from_email='sofi2darling@gmail.com',
        to_emails=to_email,
        subject='Reminder',
        plain_text_content=message
    )
    sg.send(email)