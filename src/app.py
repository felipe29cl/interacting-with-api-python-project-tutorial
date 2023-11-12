from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import datetime
import pandas as pd
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

spotify_uri = 'spotify:artist:3yIbPI61iAhMptDnfnyScb'

con = spotipy.Spotify(auth_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret))
results = con.artist_top_tracks(spotify_uri)
tracks = results['tracks']

for track in tracks:
    
    print('track    : ' + track['name'])
    print('duration_min    : ' + str(datetime.timedelta(milliseconds=track['duration_ms'])))
    print('popularity    : ' + str(track['popularity']))
    print()

tracks_df = pd.DataFrame.from_records(tracks)
tracks_df.sort_values(['popularity'],inplace=True)
print(tracks_df.head(3))