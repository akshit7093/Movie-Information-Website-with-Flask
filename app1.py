from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

def init_db():
    with app.app_context():
        db.create_all()

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    poster_url = db.Column(db.String(200))
    poster_thumbnail_url = db.Column(db.String(200))
    wide_gif_url = db.Column(db.String(200))
    rating = db.Column(db.Float, default=0.0)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    movie = db.relationship('Movie', backref=db.backref('reviews', lazy=True))

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    movies = Movie.query.all()
    return render_template('home.html', movies=movies)

@app.route('/movie/<int:movie_id>')
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    reviews = Review.query.filter_by(movie_id=movie_id).order_by(Review.created_at.desc()).all()
    return render_template('movie_detail.html', movie=movie, reviews=reviews)

@app.route('/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        new_movie = Movie(
            title=request.form['title'],
            director=request.form['director'],
            release_year=request.form['release_year'],
            description=request.form['description'],
            poster_url=request.form['poster_url'],
            poster_thumbnail_url=request.form['poster_thumbnail_url'],
            wide_gif_url=request.form['wide_gif_url']
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_movie.html')


@app.route('/movie/<int:movie_id>/add_review', methods=['POST'])
def add_review(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    new_review = Review(
        movie_id=movie_id,
        author=request.form['author'],
        content=request.form['content'],
        rating=request.form['rating']
    )
    db.session.add(new_review)
    db.session.commit()
    return redirect(url_for('movie_detail', movie_id=movie_id))

@app.route('/search')
def search():
    query = request.args.get('query', '')
    movies = Movie.query.filter(Movie.title.contains(query) | Movie.director.contains(query)).all()
    return render_template('search_results.html', movies=movies, query=query)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
