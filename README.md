
# Spotify-lite System

This project is a designed to mimic core functionalities of a music streaming service like Spotify. It provides a RESTful API for managing artists, albums, tracks, and user-created playlists.
## Key Features

- **RESTful API**: Exposes endpoints for managing music data and playlists.
- **Data Persistence**: Uses a MySQL database to store and manage all application data.
- **Object-Relational Mapping (ORM)**: SQLAlchemy is used to interact with the database using Python objects, abstracting away raw SQL.
- **Data Validation**: Pydantic ensures data integrity for all API requests and responses.
- **Command-Line Interface (CLI)**: A simple tool to easily populate the database with initial data.
- **Testing**: A comprehensive test suite using `pytest` to ensure all API endpoints function as expected.

## Technology Stack

- **Backend Framework**: `FastAPI` (Python)
- **Database**: `MySQL`
- **Database ORM**: `SQLAlchemy`
- **Data Validation**: `Pydantic`
- **Web Server**: `Uvicorn`
- **Testing**: `pytest`, `requests`

## Setup and Installation

 Steps to get the project running on your local machine.

### 1. Prerequisites

- Python 3.8+ installed on your system.
- MySQL server installed and running.

### 2. Clone the Repository

cd spotify-lite-system


### 3\. Set Up the Virtual Environment

It is highly recommended to use a virtual environment to manage dependencies.


python3 -m venv venv
 `venv\Scripts\activate`


### 4\. Install Dependencies

```bash
pip install -r requirements.txt
```
### 5\. Configure the Database

  - **Create a MySQL Database**:
    ```sql
    CREATE DATABASE spotify_lite;
    ```
  - **Update the Connection String**: Open `database.py` and modify the `DATABASE_URL` with your MySQL credentials.
    ```python
    DATABASE_URL = "mysql+mysqlconnector://<user>:<password>@localhost:3306/spotify_lite"
    ```

### 6\. Create Database Tables

Run the `create_tables.py` script to automatically create all the necessary tables based on your SQLAlchemy models.

```bash
python create_tables.py
```

### 7\. Populate the Database with Seed Data

Use the `dataset.py` script to insert a large amount of sample data into the database.

```bash
python dataset.py
```

## Running the Application

To start the FastAPI server, run the following command from the root directory:

```bash
uvicorn main:app --reload
```

The server will run at `http://127.0.0.1:8000`.

## API Documentation

FastAPI automatically generates interactive API documentation. You can access it at:

  - **Swagger UI**: `http://127.0.0.1:8000/docs`
  - **ReDoc**: `http://127.0.0.1:8000/redoc`

## Testing

To run the full test suite, use `pytest`:

```bash
pytest
```

## Contributing

**Author**: --Aditya Badiger
