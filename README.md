# Spotify-lite System

This project is a backend system designed to mimic core functionalities of a music streaming service like Spotify. It provides a RESTful API for managing artists, albums, tracks, and user-created playlists.

The system is built using a modern, high-performance tech stack, emphasizing a clear architecture, data validation, and a robust database solution.

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

## Project Structure

The project is organized into several key files to maintain a clear separation of concerns:

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

### 1. Prerequisites

- Python 3.8+ installed on your system.
- MySQL server installed and running.

### 2. Clone the Repository

```bash
git clone <your-repository-url>
cd spotify-lite-syste
.
### 2. Clone the Repository
