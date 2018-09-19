# -*- coding: utf-8 -*-
import scrapy
from crawler.items import AkutagawaPrizeItem


# Scrapyスパイダー
class AkutagawaPrizeSpider(scrapy.Spider):
    name = 'akutagawa_prize_list'
    allowed_domains = ['www.bunshun.co.jp']
    start_urls = ["http://www.bunshun.co.jp/shinkoukai/award/akutagawa/list.html"]

    # HTTPレスポンスのパース
    def parse(self, response):
        contents = response.xpath('//*[@id="myTabContent"]')
        tabIds = contents.xpath('div/@id').extract()

        for tabId in tabIds:
            # データ抽出
            tab = contents.xpath('div[@id="' + tabId + '"]')
            nos = remove_header(tab.xpath('dl/*/span[@class="no"]/text()').extract())
            years = remove_header(tab.xpath('dl/*/span[@class="year"]/text()').extract())
            names = remove_header(tab.xpath('dl/*/span[@class="name"]/text()').extract())
            titles = tab.xpath('dl/*/span[@class="title"]/text()').extract()
            magazines = remove_header(tab.xpath('dl/*/span[@class="magazine "]/text()').extract())

            # 受賞者のない行を削除して行数を揃える
            na_indexes = [i for i, val in enumerate(names) if val == "なし"]
            remove_na_rows(nos, years, names, na_indexes)

            # データのセット
            for (_no, _year, _name, _title, _magazine) in zip(nos, years, names, titles, magazines):
                yield AkutagawaPrizeItem(no=_no, year=_year, name=_name, title=_title, magazine=_magazine)


# リストのヘッダ行削除
def remove_header(items):
    return items[1:]


# リストの指定行削除
def remove_na_rows(nos, years, names, indexes):
    for i in sorted(indexes, reverse=True):
        del nos[i], years[i], names[i]