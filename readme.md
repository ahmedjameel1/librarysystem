# Library API

## Project Overview
A simple RESTful API for managing a book library system.

## Table of Contents
- [Setup and Running Instructions](#setup-and-running-instructions)
- [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
  - [Books](#books)
  - [Authors](#authors)
  - [Search](#search)
  - [Ratings](#ratings)
  - [Dockerizing](#dockerizing)
- [Assumptions and Design Decisions](#assumptions-and-design-decisions)

## Setup and Running Instructions

1. **Clone the repository.**

    ```bash
    git clone https://github.com/ahmedjameel1/librarysystem.git
    cd librarysystem
    ```

2. **Create a virtual environment and activate it.**

    ```bash
    pipenv shell
    ```

3. **Install the dependencies.**

    ```bash
    pipenv install
    ```

4. **Set up the database and environment variables.**
    - Create a `.env` file in the root directory using the `.env.example` template.
    - Fill in the required environment variables in the `.env` file.

5. **Run the migrations.**

    ```bash
    python manage.py migrate
    ```
    ```bash
    python manage.py laod_data
    ```

6. **Run Pytest.**

    ```bash
    pytest
    ```

7. **Start the server.**

    ```bash
    python manage.py runserver --insecure
    ```

## API Endpoints

### Authentication
To access the endpoints, you either have to be authenticated or send the `APIKEY` with headers.

#### Register
- `POST /api/register/`: Register a new user.
    - **Request Body**:
        ```json
        {
            "username": "string",
            "password": "string",
            "email": "string",
            "first_name": "string",
            "last_name": "string"
        }
        ```

#### Login
- `POST /api/login/`: Log in to get an API key.
    - **Request Body**:
        ```json
        {
            "username": "string",
            "password": "string"
        }
        ```
#### Logout
- `POST /api/logout/`: logs out the user.

#### Obtain API Key
- `GET /api/api_key/`: Get the API key generated at login.

### Books

- `GET /api/books/`: Retrieve a list of all books.
- `GET /api/books/:id/`: Retrieve a single book by ID.
- `POST /api/books/`: Add a new book.
    - **Request Body**:
        ```json
        {
            "title": "string",
            "isbn": "string",
            "published_year": "integer",
            "author_id": "integer"
        }
        ```
- `PUT /api/books/:id/`: Update book information.
    - **Request Body**:
        ```json
        {
            "title": "string",
            "isbn": "string",
            "published_year": "integer",
            "author_id": "integer"
        }
        ```
- `DELETE /api/books/:id/`: Delete a book.

### Authors

- `GET /api/authors/`: Retrieve a list of all authors.
- `GET /api/authors/:id/`: Retrieve a single author by ID.
- `POST /api/authors/`: Add a new author.
    - **Request Body**:
        ```json
        {
            "name": "string",
            "birth_year": "integer"
        }
        ```
- `PUT /api/authors/:id/`: Update author information.
    - **Request Body**:
        ```json
        {
            "name": "string",
            "birth_year": "integer"
        }
        ```
- `DELETE /api/authors/:id/`: Delete an author.

### Search

- `GET /api/books/?search={query}`: Search for books by title or author name.
- `GET /api/authors/?search={query}`: Search for authors by name.

### Ratings

- `GET /api/ratings/`: Retrieve a list of all ratings for all books.
- `POST /api/ratings/`: Create a rating for a book.
    - **Request Body**:
        ```json
        {
            "user": "integer",
            "book": "integer",
            "score": "integer",
            "comment": "string"
        }
        ```
- `PUT /api/ratings/:id/`: Update a rating.
    - **Request Body**:
        ```json
        {
            "score": "integer",
            "comment": "string"
        }
        ```
- `DELETE /api/ratings/:id/`: Delete a rating.

##Dockerizing

- inside the root directory where you have `docker-compose.yml`
- open terminal and run `docker-compose build`
- then `docker-compose up`

## Assumptions and Design Decisions

- Used Django REST Framework for simplicity and robustness.
- PostgreSQL was chosen for its reliability and support for complex queries.
- Environment variables are used for configuration to enhance security and flexibility.
- API uses token-based authentication for securing endpoints.
- Basic pagination and filtering for listing endpoints.
