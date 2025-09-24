from pydantic import BaseModel
from typing import List, Optional
from datetime import date, datetime

class ArtistBase(BaseModel):
    name: str
    bio: Optional[str] = None

class ArtistCreate(ArtistBase):
    pass

class Artist(ArtistBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class AlbumBase(BaseModel):
    title: str
    release_date: date
    cover_url: Optional[str] = None

class AlbumCreate(AlbumBase):
    artist_id: int

class Album(AlbumBase):
    id: int
    artist_id: int
    
    class Config:
        orm_mode = True

class TrackBase(BaseModel):
    title: str
    duration_seconds: int
    explicit: bool

class TrackCreate(TrackBase):
    album_id: int
    artist_id: int

class Track(TrackBase):
    id: int
    album_id: int
    artist_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class PlaylistBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_public: bool = True

class PlaylistCreate(PlaylistBase):
    user_id: int

class Playlist(PlaylistBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class PlaylistTrack(BaseModel):
    playlist_id: int
    track_id: int
    position: Optional[int] = None

    class Config:
        orm_mode = True