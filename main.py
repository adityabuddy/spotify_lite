from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

import models, schemas
from database import SessionLocal, engine

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Endpoint for Artists ---
@app.get("/artists", response_model=List[schemas.Artist])
def list_artists(name: Optional[str] = None, db: Session = Depends(get_db)):
    """
    List artists, optionally filtered by name.
    """
    query = db.query(models.Artist)
    if name:
        query = query.filter(models.Artist.name.like(f"%{name}%"))
    artists = query.all()
    return artists

@app.get("/artists/{artist_id}", response_model=schemas.Artist)
def get_artist(artist_id: int, db: Session = Depends(get_db)):
    """
    Get details for a specific artist.
    """
    artist = db.query(models.Artist).filter(models.Artist.id == artist_id).first()
    if artist is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Artist not found")
    return artist
    
# --- Endpoints for Playlists ---
@app.post("/playlists", response_model=schemas.Playlist, status_code=status.HTTP_201_CREATED)
def create_playlist(playlist: schemas.PlaylistCreate, db: Session = Depends(get_db)):
    """
    Create a new playlist for a user.
    """
    # Optional: You might want to check if the user_id exists
    db_playlist = models.Playlist(
        user_id=playlist.user_id,
        title=playlist.title,
        description=playlist.description,
        is_public=playlist.is_public
    )
    db.add(db_playlist)
    db.commit()
    db.refresh(db_playlist)
    return db_playlist

@app.post("/playlists/{playlist_id}", response_model=schemas.PlaylistTrack, status_code=status.HTTP_201_CREATED)
def add_track_to_playlist(playlist_id: int, track: schemas.PlaylistTrack, db: Session = Depends(get_db)):
    """
    Add a track to a playlist.
    """
    # Check if playlist and track exist
    playlist = db.query(models.Playlist).filter(models.Playlist.id == playlist_id).first()
    track_to_add = db.query(models.Track).filter(models.Track.id == track.track_id).first()
    if not playlist or not track_to_add:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Playlist or Track not found")

    # Check for duplicate entry
    existing_entry = db.query(models.PlaylistTrack).filter(
        models.PlaylistTrack.playlist_id == playlist_id,
        models.PlaylistTrack.track_id == track.track_id
    ).first()
    if existing_entry:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Track already exists in this playlist")
    
    db_playlist_track = models.PlaylistTrack(
        playlist_id=playlist_id,
        track_id=track.track_id,
        position=track.position
    )
    db.add(db_playlist_track)
    db.commit()
    db.refresh(db_playlist_track)
    return db_playlist_track

@app.get("/playlists/{playlist_id}", response_model=schemas.Playlist)
def get_playlist(playlist_id: int, db: Session = Depends(get_db)):
    """
    Get a specific playlist and its details.
    """
    playlist = db.query(models.Playlist).filter(models.Playlist.id == playlist_id).first()
    if not playlist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Playlist not found")
    return playlist

@app.get("/playlists", response_model=List[schemas.Playlist])
def list_playlists_by_user(user_id: int, db: Session = Depends(get_db)):
    """
    List playlists by user ID.
    """
    playlists = db.query(models.Playlist).filter(models.Playlist.user_id == user_id).all()
    return playlists