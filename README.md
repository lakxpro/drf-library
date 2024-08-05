## Setup Instructions

### Prerequisites

- Docker
- Docker Compose

### Steps to Run the Project

1. Clone the repository:
    ```bash
    git clone https://github.com/lakxpro/drf-library
    cd yourrepository
    ```

2. Build and start the Docker containers:
    ```bash
    docker compose build
    docker compose up -d
    ```

4. Access the application:
    Open your web browser and go to `http://127.0.0.1:8000`.


#### Create django superuser

1. Open docker container shell    
    ```bash
    docker exec -it library_app /bin/bash
    ```

2. Inside docker container shell  create superuser
    ```bash
    python manage.py createsuperuser
    ```

#### Run tests 

1. Open docker container shell    
    ```bash
    docker exec -it library_app /bin/bash
    ```

2. Inside docker container shell  create superuser
    ```bash
    python manage.py test
    ```

#### Populate database with more data 

1. Open docker container shell    
    ```bash
    docker exec -it library_app /bin/bash
    ```
2. Inside docker container shell  populate database
    ```bash
    python manage.py fake_authors &&
    python manage.py fake_books &&
    python manage.py fake_author_book_relation &&
    ```

### Token authorization after creating superuser

- Create token django administration
- http://127.0.0.1:8000/admin/
- In section Auth Token click on add token and select user

#### Or get token from api
    ```bash
    curl -X POST http://127.0.0.1:8000/api-token-auth/ \
        -H "Content-Type: application/json" \
        -d '{"username": "<username>", "password": "<password>"}'
    ```
- You should get token example {"token":"94442b5a9d2db8dc91b0c12d95bbc465f0962d33"}

#### Token usage 
- Token authorization is required for POST, PUT, PATCH, DELETE
- Add token to header of request Authorization Token c0298a0c3d491f3285f1895f5a2a9d3538762fc8f