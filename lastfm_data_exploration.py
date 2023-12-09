from config import (
    SPOTIFY_CLIENT_ID,
    SPOTIFY_SECRET,
    LASFM_SHARED_SECRET,
    LASTFM_API_KEY,
    REDIRECT_URL,
)
import urllib.request
import json


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
    except: return 999


# print(get_similar_artists("Animals as Leaders", limit = 5))

# def legacy_find_user_top_artists(user, limit=10):
#     data = parse_json(
#         f"https://ws.audioscrobbler.com/2.0/?method=library.getartists&api_key={LASTFM_API_KEY}&user={user}&limit={limit}&format=json"
#     )
#     top_artists = data.get("artists").get("artist")
#     result = []
#     for i in top_artists:
#         name = i.get("name")
#         playcount = i.get("playcount")
#         result.append(f"{name}: {playcount} plays")
#     return result

def find_user_top_artists(user, limit=10):
    data = parse_json(
        f"https://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user=rj&api_key={LASTFM_API_KEY}&user={user}&limit={limit}&format=json"
    )
    top_artists = data.get("topartists").get("artist")
    result = []
    for i in top_artists:
        name = i.get("name")
        playcount = i.get("playcount")
        result.append(f'{name}: {playcount} plays')
    return result


def find_user_top_tracks(user, limit=10):
    data = parse_json(
        f"https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user=rj&api_key={LASTFM_API_KEY}&user={user}&limit={limit}&format=json"
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
        f'https://ws.audioscrobbler.com/2.0/?method=user.gettoptags&user=rj&api_key={LASTFM_API_KEY}&user={user}&limit={limit}&format=json'
    )
    top_tags = data.get("toptags").get("tag")
    result = []
    result_dict = {}
    for tag in top_tags:
        tag_name = tag.get('name')
        count = tag.get('count') 
        result_dict[tag_name] = count
        result.append(f'{tag_name}: {count} appearances')
    return result, result_dict


def main():
    artist = "lifhaihjlfdskhflkh"
    similar_limit = 5
    print(f"Similar artists to {artist} include:")
    print(get_similar_artists(artist, limit=similar_limit))
    user = "NotLeet"
    top_limit = 10
    print(f'The top {top_limit} artists for {user} are:')
    print(find_user_top_artists(user))
    print(f'The top {top_limit} tags for {user} are:')
    top_tags, tag_dict = find_user_top_tags("rodude666", 10)
    print(top_tags)



if __name__ == "__main__":
    main()
