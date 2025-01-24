# Event Reminder and Calendar System

A comprehensive **Event Reminder and Calendar System** designed to manage events, organize calendars, and send reminders via email using Twilio. The system is built with a microservices architecture, leveraging Django REST Framework, MongoDB, RabbitMQ, and a responsive frontend using Tailwind CSS.
The system follows a microservices architecture to ensure scalability and modularity. Each component is isolated and communicates via APIs or messaging queues.

---

<br />

## Features

- **User Authentication**: JWT-based login and signup.
- **Event Management**: Create, update, delete, and fetch events.
- **User Service**: Display calendar views with organized events to the users.
- **Reminders**: Schedule reminders and send email notifications via Twilio.
- **Microservices Architecture**: Independent services for scalability and maintainability.
- **Dockerized Deployment**: Containerized services using Docker Compose.

---
<br />

## System Architecture

### System Architecture Diagram

Microservice Architecture for Event Calandar and Reminder System

![alt text](<systeme_architectures.png>)
All services are independent and follow the Microservice architecture. Communication between services is facilitated through well-defined APIs.

### Components

1. **Frontend**:
   - Technology: Tailwind CSS + HTML
   - Purpose: A responsive interface for interacting with the system.

2. **Backend Services**:
   - **Event Management Service**:
     - Manages event-related CRUD operations.
   - **User Service**:
     - Provides calendar data for users.
   - **Reminder Service**:
     - Sends email notifications using Twilio.

3. **Databases**:
   - **MongoDB**:
     - Stores event, calendar, and reminder data in separate instances.
   - Databases:
     - Event Data (MongoDB 1)
     - User Data (MongoDB 2)
     - Reminder Data (MongoDB 3)

4. **Message Broker**:
   - RabbitMQ for inter-service communication.

5. **Notification System**:
   - Twilio for sending email reminders.

---
<br />

## API Endpoints

### Event Management Service
| Description          | Endpoint                  | Method |
|----------------------|---------------------------|--------|
| Create an Event      | `/api/events/create`      | POST   |
| Update an Event      | `/api/events/{id}/update` | PATCH  |
| Delete an Event      | `/api/events/{id}/delete` | DELETE |
| Get All Events       | `/api/events`            | GET    |

<br />

### Calendar Service
| Description          | Endpoint                  | Method |
|----------------------|---------------------------|--------|
| Fetch Calendar Data  | `/api/calendar/{user_id}` | GET    |

<br />

### Reminder Service
| Description          | Endpoint                  | Method |
|----------------------|---------------------------|--------|
| Add a Reminder       | `/api/reminders/add`      | POST   |
| Update a Reminder    | `/api/reminders/{id}`     | PATCH  |
| Delete a Reminder    | `/api/reminders/{id}`     | DELETE |
| Trigger Reminders    | `/api/reminders/trigger`  | POST   |

<br />

### Authentication Service
| Description       | Endpoint              | Method |
|-------------------|-----------------------|--------|
| User Login        | `/api/auth/login`    | POST   |
| User Signup       | `/api/auth/signup`   | POST   |

---
<br />

## Communication Flow

- **Inter-Service Communication**:

  - Services communicate via REST APIs.
  - Asynchronous messaging (e.g., RabbitMQ or Kafka) is planned for event-driven operations.

- **Data Sharing**:
  - Each service maintains its own database for a decentralized approach.
  - APIs are used to share required data between services.

<br />

### UML Sequence Diagram, How the services communicate

![alt text](<sequence-diagram-communication.png>)


<br />

## Scalability and Fault Tolerance

- **Horizontal Scaling**: Each service can be scaled independently.
- **Database Isolation**: Each service uses a dedicated database to ensure autonomy.
- **Resilience**: Services are loosely coupled to prevent cascading failures.

## Security

- **Authentication**: User and driver authentication via secure tokens
- **API Gateway**: Centralized API gateway for secure communication and routing.

### Docker Compose Table

| **Service Name**         | **Image**                   | **Container Name** | **Build Context**          | **Ports**        | **Depends On**        | **Environment Variables**           |
|--------------------------|-----------------------------|--------------------|---------------------------|------------------|-----------------------|-------------------------------------|
| `rabbitmq`              | `rabbitmq:3-management`    | `rabbitmq`         | N/A                       | `5672:5672`, `15672:15672` | N/A                   | `RABBITMQ_DEFAULT_USER=guest`      |
|                          |                             |                    |                           |                  |                       | `RABBITMQ_DEFAULT_PASS=guest`      |
| `user-service`       | event-service                        | N/A                | `./event-service`       | `8000:8000`     | `rabbitmq`,  | `RABBITMQ_HOST=rabbitmq`           |
| `user-service`  | user-service                        | N/A                 | `./user-service`  | `8001:8001`     | `rabbitmq`,  | `RABBITMQ_HOST=rabbitmq`           |
| `reminder-service`  | reminder-service                        | N/A                | `./reminder-service`  | `8002:8002`     | `rabbitmq`            | `RABBITMQ_HOST=rabbitmq`           |


## Installation and Deployment

### Prerequisites

- Docker (recommended for containerized deployment).

### Steps

1. Clone the repositories for all services.

   ```bash
   git clone <repository_url>
   ```

2. Set up `.env` files for each service with appropriate configurations.

3. Run services:

    ```bash
    docker-compose up --build
    ```

4. Access APIs via the centralized API Gateway.

    ```bash
    http://localhost:8080/<<service>>
    ```
    
    <br />
    
## Technologies Used

- **Frontend**: Tailwind CSS, HTML
- **Backend**: Django REST Framework, python
- **Database**: MongoDB
- **Message Broker**: RabbitMQ
- **Notifications**: Twilio
- **Containerization**: Docker, Docker Compose

   <br />

## Contributors

| Name                | ID            |
|---------------------|---------------|
| Solomon Belay       | ETS1186/13    |
| Yihune Zewdie      | ETS1318/13    |
| Yeabsira Yonas     | ETS1302/13    |
| Yididiya Amare     | ETS1312/13    |
| Yodit Tamirat      | ETS1330/13    |

<br />
