import requests
import pytest
import time

# Base URL for the FastAPI application
BASE_URL = "http://127.0.0.1:8000"

# Wait for the server to be ready
def wait_for_server():
    max_retries = 10
    for i in range(max_retries):
        try:
            requests.get(BASE_URL + "/docs")
            print("Server is ready!")
            return
        except requests.exceptions.ConnectionError:
            print(f"Waiting for server... (attempt {i+1}/{max_retries})")
            time.sleep(2)
    raise ConnectionError("Server did not start in time.")

# A test fixture to run once before all tests
@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    # This is a simple way to ensure the server is ready for testing
    # For a real project, you'd use a test database or a more robust setup
    wait_for_server()
    # No teardown needed for this simple case
    yield

def test_create_user():
    """Test creating a new user."""
    user_data = {
        "username": "testuser",
        "email": "testuser@example.com"
    }
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    # The response should be a 201 Created status
    assert response.status_code == 201
    created_user = response.json()
    assert created_user["username"] == "testuser"
    assert "id" in created_user
    pytest.user_id = created_user["id"]  # Store user_id for later tests

def test_list_artists_no_filter():
    """Test listing all artists without a filter."""
    response = requests.get(f"{BASE_URL}/artists")
    assert response.status_code == 200
    artists = response.json()
    assert isinstance(artists, list)

def test_get_nonexistent_artist():
    """Test getting an artist that does not exist."""
    response = requests.get(f"{BASE_URL}/artists/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Artist not found"

def test_create_playlist():
    """Test creating a playlist for the created user."""
    playlist_data = {
        "user_id": pytest.user_id,
        "title": "My Test Playlist",
        "description": "A playlist for testing.",
        "is_public": True
    }
    response = requests.post(f"{BASE_URL}/playlists", json=playlist_data)
    assert response.status_code == 201
    created_playlist = response.json()
    assert created_playlist["title"] == "My Test Playlist"
    pytest.playlist_id = created_playlist["id"]

def test_list_playlists_by_user():
    """Test listing playlists by a user's ID."""
    response = requests.get(f"{BASE_URL}/playlists", params={"user_id": pytest.user_id})
    assert response.status_code == 200
    playlists = response.json()
    assert len(playlists) > 0
    assert playlists[0]["user_id"] == pytest.user_id