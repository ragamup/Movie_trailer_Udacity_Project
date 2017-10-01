import webbrowser
import urllib

#Creatin a class movie with movie title, poster, trailer and story as parameters
class Movie():
    #Creatin an init function
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    #creating a function to open youtube url using webbrowser file
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

  #Creatin a class tv show with tv show title, poster, trailer and story as parameters      
class Tv():
    def __init__(self,tv_title,tv_storyline,poster_image,trailer_youtube):
        self.title = tv_title
        self.storyline = tv_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

        #creating a function to open youtube url using webbrowser file

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

        
