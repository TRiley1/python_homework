from db.run_sql import run_sql
from models.album import Album
import repositories.artist_repo as artist_repo
# I want to create an album 

def select_all():
    albums = []
    sql  = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repo.select(row['artist_id'])
        new_album = Album(row['title'], row['genre'], artist)
        albums.append(new_album)

    return albums

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s,%s,%s) RETURNING *"
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)

    id = results[0]['id']
    album.id = id
    return album 

def delete_all():
    sql = "DELETE from albums"
    run_sql(sql)

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if len(results) > 0:
        selected_artist = results[0]
        artist = artist_repo.selected_artist(['artist_id'])
        album = Album(
            selected_artist['title'],
            selected_artist['genre'],
            artist
        )

    return album