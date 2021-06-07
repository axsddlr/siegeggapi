from fastapi import FastAPI
import uvicorn
from api.scrape import SGE
from ratelimit import limits


app = FastAPI(
    title="siegeggapi",
    description="An Unofficial REST API for [siege.gg](https://www.siege.gg/), a site for Rainbow 6 Siege Esports match and news coverage",
    version="1.0.3",
    docs_url="/",
    redoc_url=None,
)
siege = SGE()

TEN_MINUTES = 600


@limits(calls=50, period=TEN_MINUTES)
@app.get("/news")
def sge_news():
    return siege.sge_recent()


@limits(calls=50, period=TEN_MINUTES)
@app.get("/rankings/{region}")
def sge_rankings(region):
    return siege.sge_rankings(region)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=3001)
