import tkinter as tk


class MovieRecommendationsGUI:
    def __init__(self, engine):
        self.engine = engine
    
    def _recommend_movies(self):
        user_ratings = []
        for movie, rating in self.entries.items():
            if rating.get() != '':
                user_ratings.append((movie, int(rating.get())))
        recommended_movies = self.engine.get_movies(user_ratings)
        self.results_label['text'] = ',\n'.join(recommended_movies)
    
    def run(self):
        self.window = tk.Tk()
        self.window.title('Movie Recommendations')

        self.entries = {}
        for idx, movie_info in enumerate(self.engine.get_top_movies()):
            label = tk.Label(self.window, text=movie_info[0], anchor='w')
            label.grid(row=idx, column=0, sticky='w', padx=10, pady=10)
            label1 = tk.Label(self.window, text=f'genre: {movie_info[1]}', anchor='w')
            label1.grid(row=idx, column=1, sticky='w', padx=10, pady=10)

            entry = tk.Entry(self.window, width=5)
            entry.grid(row=idx, column=2, padx=10, pady=10)
            self.entries[movie_info[0]] = entry

        submit_button = tk.Button(self.window, text='Submit', command=self._recommend_movies)
        submit_button.grid(row=len(self.engine.user_ratings.columns), column=0, columnspan=2, padx=10, pady=10)

        self.results_label = tk.Label(self.window, text='')
        self.results_label.grid(row=len(self.engine.user_ratings.columns) + 1, column=0, columnspan=2, padx=10, pady=10)
        
        self.window.mainloop()






