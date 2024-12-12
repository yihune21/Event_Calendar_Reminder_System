# Event Calendar and Reminder System (Microservices Architecture)

## Overview
This project is a microservices-based Event Calendar and Reminder System. It is built using Django, Django REST framework, PostgreSQL, and RabbitMQ for inter-service communication. Each microservice operates independently and communicates via RESTful APIs and RabbitMQ.

### Microservices Overview
1. Calendar Service: Manages event creation, updates, and deletion.
2. Reminder Service: Manages scheduling and sending reminders.
3. User Service: Handles user registration, authentication, and preferences.

---

## Table of Contents
- [Event Calendar and Reminder System (Microservices Architecture)](#event-calendar-and-reminder-system-microservices-architecture)
  - [Overview](#overview)
      - [Microservices Overview](#microservices-overview)
        - [Table of Contents](#table-of-contents)
	  - [Getting Started](#getting-started)
	      - [Prerequisites](#prerequisites)
	          - [Microservices](#microservices)
		        - [Calendar Service](#calendar-service)
			      - [Reminder Service](#reminder-service)
			            - [User Service](#user-service)
				      - [Environment Setup](#environment-setup)
				          - [Docker Setup](#docker-setup)

					  ---

					  ## Getting Started

					  ### Prerequisites
					  - Docker and Docker Compose
					  - Python 3.10+
					  - PostgreSQL (Dockerized in this setup)
					  - RabbitMQ for message queuing

					  ### Microservices

					  #### Calendar Service
					  Handles all operations related to event creation, update, retrieval, and deletion.

					  #### Reminder Service
					  Schedules reminders based on events created in the Calendar Service. Utilizes RabbitMQ for queuing reminders.

					  #### User Service
					  Manages user accounts, login, and preference settings for reminders.

					  ---

					  ## Environment Setup

					  ### Docker Setup
					  The project is dockerized. Use the docker-compose.yml to start all services.

					  `bash
					  docker-compose up --build`

