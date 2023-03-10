from movie_rec_gui import MovieRecommendationsGUI
from recommendation_engine import RecommendationEngine


engine = RecommendationEngine('ratings.csv', 'movies.csv')
gui = MovieRecommendationsGUI(engine)
gui.run()