import sys
from datetime import date
from database import SessionLocal
from models import Artist, Album, Track

# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def add_artist(name: str, bio: str):
    """Adds a new artist to the database."""
    db = next(get_db())
    new_artist = Artist(name=name, bio=bio)
    db.add(new_artist)
    db.commit()
    db.refresh(new_artist)
    print(f"Artist '{new_artist.name}' with ID {new_artist.id} added successfully.")

def add_album(artist_id: int, title: str, release_date: str, cover_url: str):
    """Adds a new album to the database."""
    db = next(get_db())
    # Check if artist exists
    artist = db.query(Artist).filter(Artist.id == artist_id).first()
    if not artist:
        print(f"Error: Artist with ID {artist_id} not found.")
        return

    release_date_obj = date.fromisoformat(release_date)
    new_album = Album(artist_id=artist_id, title=title, release_date=release_date_obj, cover_url=cover_url)
    db.add(new_album)
    db.commit()
    db.refresh(new_album)
    print(f"Album '{new_album.title}' for artist '{artist.name}' with ID {new_album.id} added successfully.")

def add_track(album_id: int, artist_id: int, title: str, duration: int, explicit: bool):
    """Adds a new track to the database."""
    db = next(get_db())
    # Check if album and artist exist
    album = db.query(Album).filter(Album.id == album_id).first()
    artist = db.query(Artist).filter(Artist.id == artist_id).first()
    if not album:
        print(f"Error: Album with ID {album_id} not found.")
        return
    if not artist:
        print(f"Error: Artist with ID {artist_id} not found.")
        return

    new_track = Track(
        album_id=album_id,
        artist_id=artist_id,
        title=title,
        duration_seconds=duration,
        explicit=explicit
    )
    db.add(new_track)
    db.commit()
    db.refresh(new_track)
    print(f"Track '{new_track.title}' added successfully.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cli.py <command> [args]")
        print("Commands: add_artist, add_album, add_track")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    try:
        if command == "add_artist":
            add_artist(name=args[0], bio=args[1])
        elif command == "add_album":
            add_album(artist_id=int(args[0]), title=args[1], release_date=args[2], cover_url=args[3])
        elif command == "add_track":
            add_track(album_id=int(args[0]), artist_id=int(args[1]), title=args[2], duration=int(args[3]), explicit=args[4].lower() == 'true')
        else:
            print(f"Unknown command: {command}")
    except IndexError:
        print("Error: Not enough arguments provided for the command.")
    except Exception as e:
        print(f"An error occurred: {e}")