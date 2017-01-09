import webbrowser


# this is a class for movie blueprint
class Movie():
    """this the movie class"""
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 youtube_trailer):
        self.title = movie_title  # movie title
        self.storyline = movie_storyline  # storyline
        self.poster_image_url = poster_image  # poster image
        self.trailer_youtube_url = youtube_trailer  # youtube trailer url

    def show_trailer(self):
        """open a trailer in webbrowser"""
        webbrowser.open(self.youtube_trailer_url)
