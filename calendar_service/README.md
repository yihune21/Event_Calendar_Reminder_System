# Calendar Service

## Description
This microservice handles event management with scheduled reminders.

## Features
- Create, read, update, and delete events.
- Asynchronous reminders using Celery and RabbitMQ.

## API Endpoints

- **GET /api/events/** - List all events for the authenticated user
- **POST /api/events/** - Create a new event (also schedules a reminder)
- **GET /api/events/<id>/** - Retrieve event details
- **PUT /api/events/<id>/** - Update an existing event
- **DELETE /api/events/<id>/** - Delete an event

## Reminder Integration
Each event scheduled will automatically trigger a reminder notification sent 1 hour before the event start time.

## Getting Started

1. Install Dependencies
   `bash
      pip install -r requirements.txt


