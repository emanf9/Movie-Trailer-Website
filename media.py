class Movie:
    """Movie is a class that takes in the title, plotline, poster image,
        and trailer, and creates an object that represents a movie"""

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """This constructor assigns the title, plotline, poster image,
           and trailer to variables"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
