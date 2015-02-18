#Import the Media file for access to Movie Class definitions.
import media
import fresh_tomatoes

#Variable for a movie initializing the Movie class to create a new movie object.
the_lego_movie = media.Movie("The Lego Movie",
							 "A lego that makes a difference.",
							 "2014",
							 "Chris Pratt, Elizabeth Banks, Will Arnett, Morgan Freeman, Will Ferrell, Charlie Day",
							 "http://ia.media-imdb.com/images/M/MV5BMTg4MDk1ODExN15BMl5BanBnXkFtZTgwNzIyNjg3MDE@._V1_SY1200_CR90,0,630,1200_AL_.jpg",
							 "https://www.youtube.com/watch?v=fZ_JOBCLF-I",)

mr_turner = media.Movie("Mr. Turner",
							 "A film about painting, and drama.",
							 "2014",
							 "Timothy Spall, Marion Bailey, Lesley Manville, Paul Jesson, Dorothy Atkinson, Ruth Sheen",
							 "http://ia.media-imdb.com/images/M/MV5BMjUzNTg0MzM3NF5BMl5BanBnXkFtZTgwNDg3NTY5MjE@._V1_SY317_CR0,0,214,317_AL_.jpg",
							 "https://www.youtube.com/watch?v=Tn4zSR_5ioI",)

the_wrestler = media.Movie("The Wrestler",
							 "About a wrestler, and his retirement.",
							 "2008",
							 "Mickey Rourke, Evan Rachel Wood, Todd Barry, Marisa Tomei, Ernest Miller, Mark Margolis",
							 "https://jmichaelrios.files.wordpress.com/2013/05/thewrestler.jpg",
							 "www.youtube.com/watch?v=61-GFxjTyV0",)

monsieur_lazhar = media.Movie("Monsieur Lazhar",
							 "A foreign film about culture.",
							 "2012",
							 "Mohamed Fellag, Emilien Neron, Seddik Benslimane, Sophie Nelisse, Danielle Proulx, Brigitte Poupart",
							 "http://www.dvdsreleasedates.com/covers/monsieur-lazhar-dvd-cover-50.jpg",
							 "https://www.youtube.com/watch?v=gjNCkxnT-xE",)

the_maze_runner = media.Movie("The Maze Runner",
							 "A film about youth and adventure.",
							 "2014",
							 "Dylan O'Brien, Thomas Brodie-Sangster, Aml Ameen, Kaya Scodelario, Will Poulter, Ki Hong Lee",
							 "http://content9.flixster.com/movie/11/18/91/11189195_det.jpg",
							 "https://www.youtube.com/watch?v=64-iSYVmMVY",)

video_games_the_movie = media.Movie("Video Games: The Movie",
							 "Documentary about Video Games.",
							 "2014",
							 "Sean Astin, Cliff Bleszinski, Al Alcorn, Nolan Bushnell, Zach Braff, Peter Armstrong",
							 "http://ia.media-imdb.com/images/M/MV5BMjI2NzQ0MTI1Ml5BMl5BanBnXkFtZTgwNzMyMDE2MDE@._V1_SX640_SY720_.jpg",
							 "www.youtube.com/watch?v=ETSKGdtrMK8",)
#Movies array to be passed in as an argument to the fresh_tomatoes function. Output will generate HTML/CSS content for movies page.
movies = [the_lego_movie, mr_turner, the_wrestler, monsieur_lazhar, the_maze_runner, video_games_the_movie]
fresh_tomatoes.open_movies_page(movies)