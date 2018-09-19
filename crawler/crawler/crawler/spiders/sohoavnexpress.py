# -*- coding: utf8 -*-
from detail_scraper import DetailScraper


class SohoaVnexpressNet(DetailScraper):
    name = "sohoa"
    urls = [
            'https://sohoa.vnexpress.net/tin-tuc/doi-song-so/tap-chi-co-chu-ky-steve-jobs-duoc-ban-gia-50-000-usd-3662652.html',
        ]
    xpaths = {
        "title": '//*[@id="col_sticky"]/h1/text()',
        "description": '//*[@id="col_sticky"]/h2',
        "content": '//*[@id="col_sticky"]/article',
        "author": '//*[@id="col_sticky"]/article/p[5]/strong/text()',
        "publish_date": '//*[@id="col_sticky"]/header/span/text()'
    }

    def __init__(self):
        DetailScraper.__init__(self)
