# 96. Review the Course Management API you built. Identify 3–4 bounded contexts — groups of related functionality that could be independent services. 
# Document them in a README.md as: Service Name | Responsibility | Endpoints it owns | Database it owns.

# 97. The natural decomposition: Student Service (student CRUD, enrollment), Course Service (department and course CRUD), 
# Auth Service (registration, login, token validation), Notification Service (email confirmations).

'''
| Service              | Responsibility                           | Endpoints          | Database        |
| -------------------- | ---------------------------------------- | ------------------ | --------------- |
| Auth Service         | User registration, login, JWT validation | `/auth/*`          | auth.db         |
| Course Service       | Course CRUD, Departments                 | `/courses/*`       | course.db       |
| Student Service      | Student CRUD, Enrollments                | `/students/*`      | student.db      |
| Notification Service | Email confirmations                      | `/notifications/*` | notification.db |
'''

# 98. Create two minimal Flask apps in separate folders: course_service/ (port 5001) and student_service/ (port 5002). 
# Each has its own database and its own subset of the original endpoints.

# 99. Verify each service runs independently: python app.py in each folder. Confirm they do not share a database.

# 100. Add an enrollment endpoint to Student Service: POST /api/students/{id}/enroll. 
# This endpoint needs to verify the course exists — it must call Course Service's GET /api/courses/{id}/ using Python's requests library.

# 101. Handle the scenario where Course Service is unavailable:
# catch the ConnectionError and return 503 Service Unavailable with a descriptive message.

# 102. Create a simple API Gateway using Flask (gateway/ folder, port 5000): a single Flask app that proxies requests to the correct service.
# /api/courses/* → Course Service, /api/students/* → Student Service. Use requests.request() to forward calls.

# 103. Test the full flow through the gateway: POST http://localhost:5000/api/students/1/enroll with a course_id — 
# the gateway routes to Student Service, which calls Course Service to verify the course.

# 104. Document in a README: what are the trade-offs of synchronous (HTTP) vs asynchronous (message queue) 
# inter-service communication? When would you use a message queue like RabbitMQ or Kafka instead?

'''
Synchronous Communication (HTTP):
- One service directly calls another service using an HTTP request and waits for an immediate response.
- Used in this project: Student Service calls Course Service to verify that a course exists before creating an enrollment.

    * Advantages:
        - Simple to implement and debug.
        - Immediate response to the client.
        - Suitable when the result is required instantly.

    * Disadvantages:
        - Tight coupling between services.
        - Caller must wait for the response.
        - Failure of one service can affect another.
        - Increased latency.

Asynchronous Communication (Message Queue):
- A service publishes a message to a message broker (e.g., RabbitMQ or Kafka) without waiting for another service to process it.
- Consumers process messages independently.

    * Advantages:
        - Loose coupling between services.
        - Better scalability and fault tolerance.
        - Services continue operating even if consumers are temporarily unavailable.
        - Ideal for background processing.

    * Disadvantages:
        - More complex architecture.
        - Requires additional infrastructure.
        - Eventual consistency instead of immediate consistency.
        - Harder to trace and debug.

RabbitMQ:
    - Best for task queues, email notifications, payment processing,
    and background jobs.

Kafka:
    - Best for event streaming, analytics, activity tracking, log aggregation, and real-time data pipelines.

This project uses synchronous HTTP communication because enrollment requires immediate validation that a course exists before it can be created.

Message queues would be preferred for operations that do not require an immediate response, 
such as sending emails, notifications, logging, analytics, or report generation.
'''