# -*- coding: utf-8 -*-
import scrapy


class CardsSpider(scrapy.Spider):
    name = "cards"
    allowed_domains = ["d3go.com"]
    start_urls = (
        'https://d3go.com/mtgpq-card-list-origins/',
        'https://d3go.com/mtgpq-card-list-battle-for-zendikar/',
        'https://d3go.com/mtgpq-card-list-oath-of-the-gatewatch/',
        'https://d3go.com/mtgpq-card-list-shadows-over-innistrad/',
        'https://d3go.com/mtgpq-card-list-eldritch-moon/',
        'https://d3go.com/mtgpq-card-list-kaladesh/',
    )

    def parse(self, response):
        for card in response.css('div.cardWrapper'):
            detailtexts = card.css('div.card-details div ::text').extract()
            yield {
                'title': card.css('h3 ::text').extract_first(),
                'type': detailtexts[5].strip(),
                'rarity': detailtexts[8].strip(),
                'deck': detailtexts[2].strip(),
                'cardText': detailtexts[10].strip(),
                'imgUrl': card.css('img.card-art ::attr(data-original)').extract_first()
                }
