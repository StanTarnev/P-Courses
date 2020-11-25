from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

def save(album):
    sql = "INSERT INTO albums (title, artist_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.artist_id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album


def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        album = Album(row['title'], row['artist_id'], row['genre'], row['id'])
        albums.append(album)

    return albums


def artist(album):
    artist = None

    sql = "SELECT * FROM artists WHERE id = %s"
    values = [album.artist_id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['name'])

    return artist


### EXTENSIONS

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def select(id):
    album = None

    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None:
        result = result[0]
        album = Album(result['title'], result['artist_id'], result['genre'], result['id'])

    return album


def update(album):
    sql = "UPDATE albums SET (title, artist_id, genre) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.artist_id, album.genre, album.id]
    run_sql(sql, values)
