from config import (
    SPOTIFY_CLIENT_ID,
    SPOTIFY_SECRET,
    LASFM_SHARED_SECRET,
    LASTFM_API_KEY,
    REDIRECT_URL,
)
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import urllib.request
import json
from wordcloud import WordCloud  # https://amueller.github.io/word_cloud/references.html


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_SECRET,
        redirect_uri="http://localhost:5000",
        scope="user-top-read",
    )
)


def get_top_artists(time_frame="medium_term", limit=10):
    result = []
    top_artists = sp.current_user_top_artists(limit=limit, time_range=time_frame)
    for i in range(len(top_artists["items"])):
        result.append(f'{top_artists["items"][i].get("name")}')
    return result


def get_top_tracks(time_frame="medium_term", limit=10):
    result = []
    top_tracks = sp.current_user_top_tracks(limit=limit, time_range=time_frame)
    items = top_tracks["items"]
    for i in range(len(items)):
        trackname = items[i].get("name")
        artist = ""
        artist += items[i]["artists"][0].get("name")
        result.append(f"{trackname} - {artist}")
    return result


def parse_json(url):
    with urllib.request.urlopen(url) as f:
        response_text = f.read().decode("utf-8")
        parsed = json.loads(response_text)
    return parsed


def get_similar_artists(artist, limit=10):
    try:
        artist = artist.replace(" ", "+")
        data = parse_json(
            f"https://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist={artist}&api_key={LASTFM_API_KEY}&limit={limit}&autocorrect=1&format=json"
        )
        similars = data.get("similarartists").get("artist")
        result = []
        for i in similars:
            name = i.get("name")
            result.append(name)
        return result
    except:
        return 999


def find_user_top_artists(user, limit=10):
    data = parse_json(
        f"https://ws.audioscrobbler.com/2.0/?method=user.gettopartists&api_key={LASTFM_API_KEY}&user={user}&limit={limit}&format=json"
    )
    top_artists = data.get("topartists").get("artist")
    result = []
    for i in top_artists:
        name = i.get("name")
        playcount = i.get("playcount")
        result.append(f"{name}: {playcount} plays")
    return result


def find_user_top_tracks(user, limit=10):
    data = parse_json(
        f"https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&api_key={LASTFM_API_KEY}&user={user}&limit={limit}&format=json"
    )
    top_artists = data.get("toptracks").get("track")
    result = []
    for i in top_artists:
        name = i.get("name")
        playcount = i.get("playcount")
        result.append(f"{name}: {playcount} plays")
    return result

def find_user_top_tags(user, limit = 25):
    data = parse_json(
        f'https://ws.audioscrobbler.com/2.0/?method=user.gettoptags&api_key={LASTFM_API_KEY}&user={user}&limit={limit}&format=json'
    )
    top_tags = data.get("toptags").get("tag")
    result = []
    result_dict = {}
    for tag in top_tags:
        tag_name = tag.get('name')
        count = tag.get('count') 
        result_dict[tag_name] = int(count)
        result.append(f'{tag_name}: {count} appearances')
    return result, result_dict

def top_tags_word_cloud(user, limit = 25):
    _, tag_dict = find_user_top_tags(user, limit)
    tag_cloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(tag_dict)
    return tag_cloud




def main():
    artist = "lifhaihjlfdskhflkh"
    similar_limit = 5
    print(f"Similar artists to {artist} include:")
    print(get_similar_artists(artist, limit=similar_limit))
    user = "NotLeet"
    top_limit = 4
    print(f"The top {top_limit} artists for {user} are:")
    print(find_user_top_artists(user, top_limit))
    print(f"The top {top_limit} tracks for {user} are:")
    print(find_user_top_tracks(user, top_limit))
    top_tags_word_cloud(user)


if __name__ == "__main__":
    main()
