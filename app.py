from flask import Flask, render_template, request, redirect, url_for
from lastfm_data_exploration import get_similar_artists
from spotify_data_exploration import get_top_tracks, get_top_artists


"""BEGIN FUNCTIONALITY"""

app = Flask(__name__)


@app.route("/")
def index():
    """
    returns the home page using render template
    """

    return render_template("/index.html/")

@app.route("/similar_artists")
def prompt_similar_artists():
    return render_template('/similar_artists_prompt.html')

@app.route("/result", methods=["POST"])
def result():
    query = request.form["query"]
    results = get_similar_artists(query)
    if results == 999:
        return redirect(url_for("error", query = query))
    else:
        return render_template("/similar_artists_result.html", QUERY=query, RESULT=results)


@app.route("/error", methods=["GET","POST"])
def error():
    query = request.args["query"]
    return render_template("/error.html", QUERY=query)


if __name__ == "__main__":
    app.run(debug=True)
