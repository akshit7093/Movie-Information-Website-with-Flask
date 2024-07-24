# Movie-Information-Website-with-Flask
# Movie Database

A Flask-based web application for managing and displaying a movie database. This application allows users to view a list of movies, see detailed information about each movie, and add new movies to the database.

## Features

- View a list of movies with their thumbnails and wide thumbnails.
- View detailed information about each movie.
- Play trailers if the wide thumbnail URL is a YouTube link.
- Add new movies to the database.

## Requirements

- Python 3.x
- Flask
- SQLAlchemy
- SQLite

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/moviedatabase.git
    cd Movie-Information-Website-with-Flask
    ```

2. Create a virtual environment:

    ```sh
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```



## Usage

1. Run the Flask application:

    ```sh
    flask run
    ```

2. Open your web browser and go to:

    ```
    http://127.0.0.1:5000
    ```

## Project Structure

- `app1.py`: The main application file.
- `templates/`: Contains HTML templates.
- `static/`: Contains static files like CSS and JavaScript.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
