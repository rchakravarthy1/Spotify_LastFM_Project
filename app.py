from flask import Flask, render_template, request, redirect, url_for
from main import (
    get_similar_artists,
    get_top_tracks,
    get_top_artists,
    find_user_top_artists,
    find_user_top_tracks,
    find_user_top_tags,
    top_tags_word_cloud,
)
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIFY_CLIENT_ID, SPOTIFY_SECRET


"""BEGIN FUNCTIONALITY"""

app = Flask(__name__)


@app.route("/")
def index():
    """
    returns the home page using render template
    """
    return render_template("/index.html/")


@app.route("/lastfm_splash")
def lastfm_splash():
    return render_template("/lastfm_splash.html")


@app.route("/lastfm_top_artists", methods=["GET", "POST"])
def lastfm_top_artists():
    try:
        username = request.form.get("username", " ")
        limit = request.form["limit"]
        result = find_user_top_artists(username, limit)
        return render_template(
            "/lastfm_top_artists.html", RESULT=result, LIMIT=limit, USERNAME=username
        )
    except: return redirect(url_for("error", query = request.form.get("username", " ")))


@app.route("/lastfm_top_tracks", methods=["GET", "POST"])
def lastfm_top_tracks():
    try:
        username = request.form.get("username", " ")
        limit = request.form["limit"]
        result = find_user_top_tracks(username, limit)
        return render_template(
            "/lastfm_top_tracks.html", RESULT=result, LIMIT=limit, USERNAME=username
        )
    except: return redirect(url_for("error", query = request.form.get("username", " ")))



@app.route("/lastfm_top_tags", methods=["GET", "POST"])
def lastfm_top_tags():
    try: 
        username = request.form.get("username", " ")
        limit = request.form["limit"]
        result, tagdict = find_user_top_tags(username, limit)
        wordcloud = top_tags_word_cloud(username, limit)
        wordcloud.to_file("static/tag_cloud.png")
        return render_template(
            "/lastfm_top_tags.html",
            RESULT=result,
            LIMIT=limit,
            USERNAME=username,
            WORDCLOUD=wordcloud,
        )
    except: return redirect(url_for("error", query = request.form.get("username", " ")))


@app.route("/similar_artists_prompt")
def prompt_similar_artists():
    return render_template("/similar_artists_prompt.html")


@app.route("/similar_artists_result", methods=["POST"])
def result():
    query = request.form["query"]
    result = get_similar_artists(query)
    if result == 999:
        return redirect(url_for("error", query=query))
    else:
        return render_template(
            "/similar_artists_result.html", QUERY=query, RESULT=result
        )


@app.route("/my_top_artists_prompt")
def prompt_top_artists():
    return render_template("my_top_artists_prompt.html")


@app.route("/my_top_tracks_prompt")
def prompt_top_tracks():
    return render_template("my_top_tracks_prompt.html")


@app.route("/my_top_artists_result", methods=["GET", "POST"])
def result_top_artist():
    try:
        timeframe = request.form["timeframe"]
        if request.form["limit"]:
            limit = request.form["limit"]
            if int(limit) > 50:
                limit = 50
        else:
            limit = 10  # if the user deletes the default value, default back to 10
        result = get_top_artists(timeframe, limit)
        time_formatted = timeframe.replace("_", " ")
        return render_template(
            "my_top_artists_result.html",
            TIMEFRAME=time_formatted,
            LIMIT=limit,
            RESULT=result,
        )
    except: return redirect("/wip")


@app.route("/my_top_tracks_result", methods=["GET", "POST"])
def result_top_tracks():
    try:
        timeframe = request.form["timeframe"]
        if request.form["limit"]:
            limit = request.form["limit"]
        else:
            limit = 10  # if the user deletes the default value, default back to 10
        time_formatted = timeframe.replace("_", " ")
        result = get_top_tracks(timeframe, limit)
        return render_template(
            "my_top_tracks_result.html",
            TIMEFRAME=time_formatted,
            LIMIT=limit,
            RESULT=result,
        )
    except: return redirect("/wip")


@app.route("/error", methods=["GET", "POST"])
def error():
    query = request.args["query"]
    return render_template("/error.html", QUERY=query)

@app.route("/wip")
def wip():
    return render_template('/wip.html')

if __name__ == "__main__":
    app.run(debug=True)
