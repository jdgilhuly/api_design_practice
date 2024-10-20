# Event Management System API

## Overview

This Event Management System API is a robust backend solution for managing events, user registrations, and ticket generation. Built with FastAPI and SQLAlchemy, it provides a scalable and efficient platform for event organizers and attendees.

## Features

- **User Management**: Registration, authentication, and profile management
- **Event Management**: Create, read, update, and delete events
- **Event Registration**: Allow users to register for events
- **Ticket Management**: Generate and manage tickets for registered users
- **Role-Based Access Control**: Differentiate between regular users and event organizers
- **API Versioning**: Structured for easy updates and backward compatibility
- **Pagination and Filtering**: Efficient data retrieval for events
- **Error Handling**: Consistent and informative error responses
- **Data Validation**: Ensure data integrity with Pydantic models
- **Rate Limiting**: Prevent API abuse
- **API Documentation**: Interactive API documentation with Swagger/OpenAPI

## Tech Stack

- **FastAPI**: High-performance web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation and settings management
- **Alembic**: Database migration tool
- **PostgreSQL**: Robust, open-source database
- **JWT**: JSON Web Tokens for secure authentication
- **Uvicorn**: ASGI server for running the application

## Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL
- pipenv (for dependency management)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/event-management-api.git
   cd event-management-api
   ```

2. Install dependencies:
   ```
   pipenv install
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory and add the following:
   ```
   DATABASE_URL=postgresql://user:password@localhost/dbname
   SECRET_KEY=your_secret_key_here
   ```

4. Run database migrations:
   ```
   alembic upgrade head
   ```

5. Start the server:
   ```
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`.

## API Documentation

Once the server is running, you can access the interactive API documentation at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing

To run tests:
