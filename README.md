# siegeggapi

An Unofficial REST API for [siege.gg](https://www.siege.gg/), a site for Rainbow 6 Siege Esports match and news coverage.

Built by [Andre Saddler](https://github.com/rehkloos/)

[![heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Current Endpoints

All endpoints are relative to https://siegeggapi.herokuapp.com.

### `/news`

- Method: `GET`
- Cached Time: 300 seconds (5 Minutes)
- Response:
  ```python
  {
      "data": {
          "status": 200,
          'segments': [
              {
                  'title': str,
                  'description': str,
                  'author': str,
                  'date': str,
                  'url_path': str,
                  'thumbnail': str
              }
          ],
      }
  }
  ```

## Installation

### Source

```
$ git clone https://github.com/rehkloos/siegeggapi/
$ cd vlrggapi
$ pip3 install -r requirements.txt
```

### Usage

```
python3 main.py
```

## Built With

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Requests](https://requests.readthedocs.io/en/master/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Flask-Caching](https://github.com/sh4nks/flask-caching)
- [gunicorn](https://gunicorn.org/)

## Contributing

Feel free to submit a [pull request](https://github.com/rehkloos/siegeggapi/pull/new/master) or an [issue](https://github.com/rehkloos/siegeggapi/issues/new)!

## License

The MIT License (MIT)
