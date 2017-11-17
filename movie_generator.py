# imports media and fresh_tomatoes in order to call their functions/classes
import media
import fresh_tomatoes

# initializes the movies with the media movie class
backstreet_boys = media.Movie(
    "Backstreet Boys: Show 'Em What You're Made Of",
    "The revered Backstreet Boys discuss the length of their career",
    "https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Backstreet_Boys_Doc_Movie_Poster.jpeg/220px-Backstreet_Boys_Doc_Movie_Poster.jpeg",  # NOQA
    "https://www.youtube.com/watch?v=bOZm93IWvgA")
kung_fu_panda = media.Movie(
    "Kung Fu Panda",
    "A dopey panda goes on a quest to master kung fu",
    "http://www.gstatic.com/tv/thumb/movieposters/175618/p175618_p_v8_ad.jpg",  # NOQA
    "https://www.youtube.com/watch?v=PXi3Mv6KMzY")
star_wars = media.Movie(
    "Star Wars",
    "A band of space adventurers embark on a journey to save a princess",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcTqRzbG-zvWPx5khd-1D9st1B7FYEq71Gbd2UdaPnrWPwVvY2PX",  # NOQA
    "https://www.youtube.com/watch?v=vZ734NWnAHA")

# creates movies array with movie objects and calls the fresh_tomatoes file
movies = [backstreet_boys, kung_fu_panda, star_wars]
fresh_tomatoes.open_movies_page(movies)
