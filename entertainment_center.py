import media
import fresh_tomatoes
police_Story = media.Movie("Police Story 2013",
                          " Story of a good police",
                          "https://upload.wikimedia.org/wikipedia/zh/1/1b/%E8%AD%A6%E5%AF%9F%E6%95%85%E4%BA%8B2013.jpg",
                          "https://www.youtube.com/watch?v=2T5Zr2YbDXo")
hero = media.Movie("Hero",
                   " Nameless hero kill the Qin",
                   "https://upload.wikimedia.org/"
                   +"wikipedia/en/0/08/Hero_poster.jpg",
                   "https://www.youtube.com/watch?v=MzMOhf4gkDA")
#testMovie.show_trailer()
movies = [police_Story,hero]
fresh_tomatoes.open_movies_page(movies)
