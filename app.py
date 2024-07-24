from flask import Flask, render_template, request, jsonify

app=Flask(__name__)

movies = {
    "the-shawshank-redemption": {
        "title": "The Shawshank Redemption",
        "director": "Frank Darabont",
        "release_year": 1994,
        "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."
    },
    "the-godfather": {
        "title": "The Godfather",
        "director": "Francis Ford Coppola",
        "release_year": 1972,
        "description": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."
    },
    "pulp-fiction": {
        "title": "Pulp Fiction",
        "director": "Quentin Tarantino",
        "release_year": 1994,
        "description": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption."
    }
}

@app.route('/')
def home():
    return render_template('home.html',movies=movies)

@app.route('/movie/<movie_id>')
def movie(movie_id):
    movie_info=movies.get(movie_id)
    if movie_info:
        return render_template('movie.html',movie=movie_info)
    else:
        return "movie not found"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)