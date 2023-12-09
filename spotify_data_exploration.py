from config import (
    SPOTIFY_CLIENT_ID,
    SPOTIFY_SECRET,
    LASFM_SHARED_SECRET,
    LASTFM_API_KEY,
    REDIRECT_URL,
)
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_SECRET,
        redirect_uri="http://localhost:5000",
        scope="user-top-read",
    )
)

def get_top_artists(time_frame = "medium_term", limit = 10):
    result = []
    top_artists = sp.current_user_top_artists(limit=limit, time_range=time_frame)
    for i in range(len(top_artists["items"])):
        result.append(f'{top_artists["items"][i].get("name")}')
    return result

def get_top_tracks(time_frame = "medium_term", limit = 10):
    result = []
    top_tracks = sp.current_user_top_tracks(limit=limit, time_range=time_frame)
    items = top_tracks['items']
    for i in range(len(items)):
        trackname = items[i].get("name")
        artist = ""
        artist+=(items[i]['artists'][0].get("name"))
        result.append(f'{trackname} - {artist}')
    return result

# print(get_top_artists("short_term"))
# print(get_top_tracks("short_term"))

print(get_top_artists())