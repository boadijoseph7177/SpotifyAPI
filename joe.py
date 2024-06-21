
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
cid = '74e84c45f7a2458595ba0e7a2949d03b'
secret = 'c1e589a3a8834764b38000bb06f73475'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager
=client_credentials_manager)

artist_name = []
track_name = []
popularity = []
track_id = []

for i in range(0,10):
    track_results = sp.search(q='year:2018', type='track', limit=10,offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])

print(artist_name)

search_query = "Afrobeats"
results = sp.search(q=search_query, type="playlist")

print('playlist information\n')
for item in results['playlists']['items']:
  print(f" - {item['name']}")  # Print playlist name