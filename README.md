# ITIL Knowledge & Collaboration Portal

This project is a centralized portal for ITIL best practices, collaborative knowledge sharing, and operational insights.

## Prerequisites

*   Docker
*   Docker Compose (v2)

## Getting Started

1.  **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd itil-portal
    ```

2.  **Build and run the containers:**

    Before running the following command, make sure you have `sudo` privileges and that the Docker daemon is running.

    ```bash
    sudo docker compose up --build
    ```

    The application will be available at [http://localhost:8000](http://localhost:8000).

3.  **Access the admin panel:**

    The admin panel is available at [http://localhost:8000/admin](http://localhost:8000/admin).

    *   **Username:** admin
    *   **Password:** admin

    *Note: The superuser is created automatically when the container starts for the first time.*

## Project Structure

```
itil-portal/
├── backend/
│   ├── Dockerfile
│   ├── manage.py
│   ├── requirements.txt
│   ├── itil_portal/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── apps/
│   │   ├── __init__.py
│   │   ├── knowledge_base/
│   │   ├── users/
│   │   └── itil_processes/
├── docs/
│   ├── architecture.md
├── docker-compose.yml
└── README.md
```

## Technology Stack

*   **Backend:** Django
*   **Database:** PostgreSQL
*   **Containerization:** Docker, Docker Compose
