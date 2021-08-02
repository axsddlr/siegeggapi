from threading import Thread
from fastapi import FastAPI
import uvicorn
from api.scrape import SGE, R6
from ratelimit import limits


app = FastAPI(
    title="siegeggapi",
    description="An Unofficial REST API for [siege.gg](https://www.siege.gg/) and ubisoft r6, a site for Rainbow 6 Siege Esports match and news coverage",
    version="1.0.4",
    docs_url="/",
    redoc_url=None,
)
siege = SGE()
r6 = R6()

TWO_MINUTES = 150


@limits(calls=250, period=TWO_MINUTES)
@app.get("/r6/{cat}", tags=["Rainbow 6: Siege"])
def r6_news(cat):
    """[categories]\n\n

    all\n
    patch-notes \n
    game-updates\n
    community\n
    esports\n
    """
    return r6.r6(cat)


@limits(calls=50, period=TWO_MINUTES)
@app.get("/esports/news", tags=["Rainbow 6: Esports"])
def sge_news():
    return siege.sge_recent()


@limits(calls=50, period=TWO_MINUTES)
@app.get("/esports/rankings/{region}", tags=["Rainbow 6: Esports"])
def sge_rankings(region):
    """[summary]

    "na": "north-america",\n
    "eu": "europe",\n
    "ap": "asia-pacific",\n
    "la": "latin-america",\n
    "oce": "oceania",\n
    "kr": "korea",\n
    "mn": "mena",\n
    """
    return siege.sge_rankings(region)


def run():
    uvicorn.run("main:app", host="0.0.0.0", port=3001)


def keep_alive():
    t = Thread(target=run)
    t.start()


if __name__ == "__main__":
    keep_alive()
