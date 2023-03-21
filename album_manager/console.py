from models.artist import Artist
from models.album  import Album

import repositories.album_repo as album_repo
import repositories.artist_repo as artist_repo

# I want to add artists to the database. 

artist1 = Artist("Bob Marley")
artist_repo.save(artist1)

artist2 = Artist("Harry Styles")
artist_repo.save(artist2)

# this result is a list that was define in artist_repo select_all()
result = artist_repo.select_all()

for artist in result: 
    print(artist.name)