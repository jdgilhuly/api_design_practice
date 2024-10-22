# Event Management System API

## Overview

This Event Management System API is a robust backend solution for managing events, user registrations, and ticket generation. Built with FastAPI and SQLAlchemy, it provides a scalable and efficient platform for event organizers and attendees.

## Project Scope

### Core Features

- **Users**: Registration, authentication, and profile management
- **Events**: Create, read, update, and delete events
- **Event Registration**: Allow users to register for events
- **Tickets**: Generate and manage tickets for registered users

### Entities/Resources

- **User**: name, email, password, roles
- **Event**: title, description, date, location, organizer
- **Registration**: user_id, event_id, status
- **Ticket**: registration_id, QR code, status

## Best Practices Implemented

- **Authentication and Authorization**:
  - JWT for authentication
  - Role-based access control (e.g., organizer vs. regular user)
- **API Versioning**: Structured for easy updates and backward compatibility
- **Pagination and Filtering**:
  - Efficient data retrieval for events (e.g., GET /events?page=2&limit=10)
  - Filtering by date, location, or organizer
- **Error Handling**: Consistent and informative error responses
- **Data Validation**: Ensure data integrity with Pydantic models
- **Rate Limiting**: Prevent API abuse
- **API Documentation**: Interactive API documentation with Swagger/OpenAPI
- **Testing**: Unit tests and integration tests for major API flows
- **Deployment**:
  - Cloud deployment ready (e.g., AWS, Heroku)
  - Docker containerization for consistent environments
- **Security Considerations**:
  - Input sanitization to prevent SQL injection
  - HTTPS enforcement for public deployments

## Tech Stack

- **FastAPI**: High-performance web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation and settings management
- **Alembic**: Database migration tool
- **PostgreSQL**: Robust, open-source database
- **JWT**: JSON Web Tokens for secure authentication
- **Redis**: For rate limiting implementation
- **Uvicorn**: ASGI server for running the application
- **Docker**: For containerization

## Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL
- Docker and Docker Compose (for containerized setup)

### Running with Docker Compose

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/event-management-api.git
   cd event-management-api
   ```

2. Build and start the containers:
   ```
   docker-compose up --build
   ```

   This command will build the Docker images and start the containers for the web application and the PostgreSQL database.

3. The API will be available at `http://localhost:8000`.

### Running Locally

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/event-management-api.git
   cd event-management-api
   ```

2. Install dependencies:
   ```
   pipenv install
   ```

3. Set up the local PostgreSQL database:
   - Create a database named "test"
   - Create a user "tester" with password "georgie"
   - Grant all privileges on the "test" database to "tester"

4. Start the application:
   ```
   pipenv run uvicorn app.main:app --reload
   ```

5. The API will be available at `http://localhost:8000`.

### Environment Variables

For local development, you can create a `.env` file in the root directory with the following content:

## API Documentation

Once the server is running, you can access the interactive API documentation at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Testing

To run tests:
```
pytest
```

## Deployment

For Docker deployment:

1. Build the Docker image:
   ```
   docker build -t event-management-api .
   ```

2. Run the container:
   ```
   docker run -p 8000:8000 event-management-api
   ```

For cloud deployment, follow the specific instructions for your chosen platform (AWS, Heroku, etc.).

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
