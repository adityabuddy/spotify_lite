#dataset.py
from datetime import date
from database import SessionLocal
from models import Artist, Album, Track

data_to_insert = [
    {
        "artist": {"name": "Taylor Swift", "bio": "American singer-songwriter."},
        "albums": [
            {
                "title": "Folklore", "release_date": "2020-07-24", "cover_url": "url_folklore",
                "tracks": [
                    {"title": "Cardigan", "duration_seconds": 250, "explicit": False},
                    {"title": "Exile", "duration_seconds": 270, "explicit": False}
                ]
            }
        ]
    },
    {
        "artist": {"name": "The Weeknd", "bio": "Canadian singer and producer."},
        "albums": [
            {
                "title": "After Hours", "release_date": "2020-03-20", "cover_url": "url_after_hours",
                "tracks": [
                    {"title": "Blinding Lights", "duration_seconds": 200, "explicit": False},
                    {"title": "Save Your Tears", "duration_seconds": 215, "explicit": False}
                ]
            }
        ]
    },
    {
        "artist": {"name": "Billie Eilish", "bio": "American singer-songwriter."},
        "albums": [
            {
                "title": "Happier Than Ever", "release_date": "2021-07-30", "cover_url": "url_happier_than_ever",
                "tracks": [
                    {"title": "Happier Than Ever", "duration_seconds": 298, "explicit": False},
                    {"title": "Bad Guy", "duration_seconds": 194, "explicit": False}
                ]
            }
        ]
    },
    {
        "artist": {"name": "Post Malone", "bio": "American rapper and singer."},
        "albums": [
            {
                "title": "Hollywood's Bleeding", "release_date": "2019-09-06", "cover_url": "url_hollywoods_bleeding",
                "tracks": [
                    {"title": "Circles", "duration_seconds": 215, "explicit": False},
                    {"title": "Sunflower", "duration_seconds": 158, "explicit": False}
                ]
            }
        ]
    },
    {
        "artist": {"name": "Beyoncé", "bio": "American singer, songwriter, and actress."},
        "albums": [
            {
                "title": "Lemonade", "release_date": "2016-04-23", "cover_url": "url_lemonade",
                "tracks": [
                    {"title": "Formation", "duration_seconds": 230, "explicit": False},
                    {"title": "Hold Up", "duration_seconds": 191, "explicit": False}
                ]
            }
        ]
    },
    {
        "artist": {"name": "Bruno Mars", "bio": "American singer and musician."},
        "albums": [
            {
                "title": "24K Magic", "release_date": "2016-11-18", "cover_url": "url_24k_magic",
                "tracks": [
                    {"title": "24K Magic", "duration_seconds": 226, "explicit": False},
                    {"title": "That's What I Like", "duration_seconds": 206, "explicit": False}
                ]
            }
        ]
    },
    {
        "artist": {"name": "Adele", "bio": "English singer-songwriter."},
        "albums": [
            {
                "title": "25", "release_date": "2015-11-20", "cover_url": "url_25",
                "tracks": [
                    {"title": "Hello", "duration_seconds": 295, "explicit": False},
                    {"title": "When We Were Young", "duration_seconds": 298, "explicit": False}
                ]
            }
        ]
    },
    {
        "artist": {"name": "Drake", "bio": "Canadian rapper and singer."},
        "albums": [
            {
                "title": "Views", "release_date": "2016-04-29", "cover_url": "url_views",
                "tracks": [
                    {"title": "One Dance", "duration_seconds": 174, "explicit": False},
                    {"title": "Hotline Bling", "duration_seconds": 267, "explicit": False}
                ]
            }
        ]
    },
    {
        "artist": {"name": "Rihanna", "bio": "Barbadian singer."},
        "albums": [
            {
                "title": "Anti", "release_date": "2016-01-28", "cover_url": "url_anti",
                "tracks": [
                    {"title": "Work", "duration_seconds": 220, "explicit": False},
                    {"title": "Needed Me", "duration_seconds": 185, "explicit": False}
                ]
            }
        ]
    },
    {
        "artist": {"name": "Eminem", "bio": "American rapper and producer."},
        "albums": [
            {
                "title": "The Marshall Mathers LP 2", "release_date": "2013-11-05", "cover_url": "url_mmlp2",
                "tracks": [
                    {"title": "Rap God", "duration_seconds": 363, "explicit": True},
                    {"title": "The Monster", "duration_seconds": 250, "explicit": False}
                ]
            }
        ]
    }
]

def bulk_insert_data():
    """Inserts all artist, album, and track data in a single transaction."""
    db = SessionLocal()
    try:
        for artist_data in data_to_insert:
            new_artist = Artist(
                name=artist_data['artist']['name'],
                bio=artist_data['artist']['bio']
            )
            db.add(new_artist)
            db.flush()

            for album_data in artist_data['albums']:
                release_date = date.fromisoformat(album_data['release_date'])
                new_album = Album(
                    artist_id=new_artist.id,
                    title=album_data['title'],
                    release_date=release_date,
                    cover_url=album_data['cover_url']
                )
                db.add(new_album)
                db.flush()

                for track_data in album_data['tracks']:
                    new_track = Track(
                        album_id=new_album.id,
                        artist_id=new_artist.id,
                        title=track_data['title'],
                        duration_seconds=track_data['duration_seconds'],
                        explicit=track_data['explicit']
                    )
                    db.add(new_track)
        
        db.commit()
        print("All data inserted successfully!")

    except Exception as e:
        db.rollback()
        print(f"An error occurred: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    bulk_insert_data()