import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist('Oasis')
artist_repository.save(artist_1)

album_1 = Album("Roll With It", artist_1.id, "Rock")
album_repository.save(album_1)
album_2 = Album("Another Album", artist_1.id, "Pop")
album_repository.save(album_2)



pdb.set_trace()
