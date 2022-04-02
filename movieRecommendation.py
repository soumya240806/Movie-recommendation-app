from flask import Flask, jsonify, request
from storage import all_movies, liked_movies, not_liked_movies, did_not_watch
from demographic_filtering import output
from content_based_filtering import get_recommendations

app = Flask(__name__)

@app.route("/get-movie")
def get_movie():
    movie_data = {
        "title": all_movies[0][19],
        "postal_link": all_movies[0][27],
        "release_date": all_movies[0][13] or "N/a",
        "duration": all_movies[0][15],
        "rating": all_movies[0][20],
        "overview": all_movies[0][9]
    }
    return jsonify({
        "data" : movie_data,
        "status" : "success"
    })

@app.route("/liked-movie", methods = ["POST"])
def liked_movie():
    movie = all_movies[0]
    liked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status": "success"
    }),201


@app.route("/unliked-movie", methods = ["POST"])
def unliked_movie():
    movie = all_movies[0]
    not_liked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status": "success"
    }),201


@app.route("/did-not-watch-movie", methods = ["POST"])
def did_not_watch_movie():
    movie = all_movies[0]
    did_not_watch.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status": "success"
    }),201


@app.route("/popular-movies", methods = ["POST"])
def popular_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    popular_movies.append(movie)
    return jsonify({
        "status": "success"
    }),201

if __name__ == "__main__":
    app.run()
