from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import htmlgenerator as hg
from recommendation_engine import RecommendationEngine

engine = RecommendationEngine("ratings.csv", "movies.csv")
top_movies = engine.get_top_movies()


def generate_HTML(movies_list):
    rows = []
    for idx, movie_info in enumerate(movies_list):
        rows.append(
            hg.TR(
                hg.TD(movie_info[0]),
                hg.TD(movie_info[1]),
                hg.TD(
                    hg.INPUT(
                        type='number',
                        id=f'rating{idx + 1}',
                        name=f'rating{idx + 1}',
                        min="0.5",
                        max="5",
                        step="0.5",
                        required=True
                    )
                )
            )
        )
    page = hg.HTML(
        hg.HEAD(
            hg.TITLE('Movie recommendations')
        ),
        hg.BODY(
            hg.H1('Movie recommendations'),
            hg.FORM(
                hg.TABLE(
                    rows[0],
                    rows[1],
                    rows[2],
                    rows[3],
                    rows[4],
                ),
                action="/recommendations",
                method="post"
            )
        )
    )
    return hg.render(page, {})


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index():
    return generate_HTML(top_movies)
