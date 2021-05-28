from flask import Flask, current_app, render_template
from flask_cors import CORS
from flask_caching import Cache
import ujson as json
from ratelimit import limits
from api.scrape import SGE

app = Flask(__name__, template_folder="frontpage")
cache = Cache(app, config={"CACHE_TYPE": "simple"})
CORS(app)
siege = SGE()

TEN_MINUTES = 600


@app.route("/")
def home():
    return render_template("index.html")


@limits(calls=50, period=TEN_MINUTES)
@cache.cached(timeout=300)
@app.route("/news", methods=["GET"])
def sge_news():
    return current_app.response_class(
        json.dumps(siege.sge_recent(), indent=4, escape_forward_slashes=False),
        mimetype="application/json",
    )


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return "Sorry, Nothing at this URL.", 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return "Sorry, unexpected error: {}".format(e), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001)
