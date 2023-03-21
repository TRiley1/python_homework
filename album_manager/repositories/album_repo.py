from db.run_sql import run_sql
from models.album import Album

# I want to create an album 

def save(album):
    sql = "INSERT INTO albums (title, genre, artist) VALUES (%s,%s,%s) RETURNING *"
    values = [album.title, album.genre, album.artist]
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
        album = Album(
            selected_artist['title'],
            selected_artist['genre'],
            selected_artist['artist']
        )

    return album