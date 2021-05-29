import requests
from bs4 import BeautifulSoup
import utils.resources as res

# from utils.HTMLReceive import r
import asyncio


class SGE:
    @staticmethod
    def sge_recent():
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": "3600",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        }
        URL = "https://siege.gg/news"
        html = requests.get(URL, headers=headers).text
        response = requests.get(URL)
        soup = BeautifulSoup(html, "html.parser")
        status = response.status_code

        base = soup.find(id="main")

        # Featured article
        featured_module = base.find_all(
            "article",
            {"class": "col-sm-12 entry d-flex align-items-stretch"},
        )
        featured_post = []
        for fmodule in featured_module:

            # url of each article

            url_path = fmodule.find("a", {"class": "card-img-top"})["href"]

            # thumbnail url of each articles
            thumbnail = fmodule.find(class_="card-img-top").find("img").get("data-src")

            # title of each article
            title = fmodule.find("h3").text.strip()

            # description of each article
            description = fmodule.find("p").text.strip()
            description = description.split("Read")[0].strip()

            footer_parent = fmodule.find(
                "div", {"class": "card-footer entry__meta text-muted"}
            )

            # author of each article
            author = footer_parent.span.a.get_text()

            # date and time of each article
            date = footer_parent.find("span", {"class": "meta__item meta__date"})[
                "title"
            ]
            featured_post.append(
                {
                    "title": title,
                    "description": description,
                    "author": author,
                    "date": date,
                    "url_path": url_path,
                    "thumbnail": thumbnail,
                }
            )

        # Older Articles
        older_posts_module = base.find_all(
            "article",
            {"class": "col-lg-6 entry d-flex align-items-stretch"},
        )
        older_posts = []
        for module in older_posts_module:

            # url of each article

            url_path = module.find("a", {"class": "card-img-top"})["href"]

            # thumbnail url of each articles
            thumbnail = module.find(class_="card-img-top").find("img").get("data-src")

            # title of each article
            title = module.find("h3").text.strip()

            # description of each article
            description = module.find("p").text.strip()
            description = description.split("Read")[0].strip()

            footer_parent = module.find(
                "div", {"class": "card-footer entry__meta text-muted"}
            )

            # author of each article
            author = footer_parent.span.a.get_text()

            # date and time of each article
            date = footer_parent.find("span", {"class": "meta__item meta__date"})[
                "title"
            ]

            older_posts.append(
                {
                    "title": title,
                    "description": description,
                    "author": author,
                    "date": date,
                    "url_path": url_path,
                    "thumbnail": thumbnail,
                }
            )

        api = {
            "featured": featured_post,
            "older_posts": older_posts,
        }

        segments = {"status": status, "segments": api}

        data = {"data": segments}

        if status != 200:
            raise Exception("API response: {}".format(status))
        return data

    @staticmethod
    def sge_rankings(region: str = ""):
        region = region
        headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Max-Age": "3600",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
        }
        URL = f"https://siege.gg/ranking?tab={region}"
        html = requests.get(URL, headers=headers).text
        response = requests.get(URL)
        soup = BeautifulSoup(html, "html.parser")
        status = response.status_code

        # id is based on region
        base = soup.find(id=f"{region}")

        rankings_module = base.find_all(
            "li",
            {"class": "ranking__item small overflow-hidden"},
        )
        rankings = []
        for rmodule in rankings_module:
            # title of each article
            org = rmodule.find(
                "h3", {"class": "ranking-item__team h3 px-1 px-md-2 mb-0"}
            ).text.strip()

            # rank # of each team
            rank = rmodule.find(
                "small", {"class": "ranking-item__rank mr-2 text-muted"}
            ).text.strip()

            # thumbnail url of each team
            thumbnail = rmodule.find("img").get("data-src")

            # rating of each team

            rating = rmodule.find("span").text.strip()

            rankings.append(
                {
                    "rank": rank,
                    "org": org,
                    "rating": rating,
                    "org_logo": thumbnail,
                }
            )

        segments = {"status": status, "segments": rankings}

        data = {"data": segments}

        if status != 200:
            raise Exception("API response: {}".format(status))
        return data
