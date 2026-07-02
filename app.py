from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load Data
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))


# Recommendation Function
def recommend(movie):

    movie = movie.strip()

    # Case-insensitive search
    movie_list = movies[movies['title'].str.lower() == movie.lower()]

    if movie_list.empty:
        return []

    movie_index = movie_list.index[0]

    distances = similarity[movie_index]

    recommended_movies = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    result = []

    for i in recommended_movies:
        result.append(movies.iloc[i[0]].title)

    return result


@app.route("/")
def home():
    return render_template(
        "index.html",
        recommendations=None
    )


@app.route("/recommend", methods=["POST"])
def recommendation():

    movie = request.form.get("movie")

    recommendations = recommend(movie)

    return render_template(
        "index.html",
        recommendations=recommendations,
        searched_movie=movie
    )


if __name__ == "__main__":
    app.run(debug=True)