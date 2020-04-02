import scrapy
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from datetime import datetime
import logging

class WineSearchSpider(scrapy.Spider):
    name = "winesearcher"
    handle_httpstatus_all = True
    with open("winesearcher_urls.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]


    def parse(self, response):
        print('*****',response.request.meta['redirect_urls'])

        # print('*****',response.request.url.split('/')[-1])

        # wine = response.xpath('//div[contains(concat(" ", normalize-space(@class), " "), " pipInfo ")]')
        # name = wine.xpath('//h1[contains(concat(" ", normalize-space(@class), " "), " pipName ")]')
        # name = name.xpath('text()').extract_first()
        # vintage = -1
        # if str.isdigit(name.split(' ')[-1]):
        #     vintage = int(name.split(' ')[-1])
        #     name = name.rsplit(' ', 1)[0]
        # abv = wine.xpath('//span[contains(concat(" ", normalize-space(@class), " "), " prodAlcoholPercent_percent ")]').xpath('text()').extract_first()
        # varietal = wine.xpath('//span[contains(concat(" ", normalize-space(@class), " "), " prodItemInfo_varietal ")]')
        # location = wine.xpath('//span[contains(concat(" ", normalize-space(@class), " "), " prodItemInfo_originText ")]')
        # price = wine.xpath('//link[contains(concat(" ", normalize-space(@class), " "), " productPrice_price-itemProp ")]')
        # try:
        #     price = response.xpath("//meta[@name='productPrice']/@content")[0].extract()
        #     price = price.split('$')[-1]
        # except IndexError:
        #     price = -1
        # try:
        #     ratings = wine.xpath("//ul[@class='wineRatings_list']")[0]
        #     ratings = ratings.xpath('.//li[contains(concat(" ", normalize-space(@class), " "), " wineRatings_listItem ")]')
        # except IndexError:
        #     ratings = []

        # wine_type = response.xpath('//li[contains(concat(" ", normalize-space(@class), " "), " prodAttr_icon ")]/@title')[0].extract()


        # yield {
        #     'url': response.url,
        #     'name': name,
        #     'vintage': vintage,
        #     'type': wine_type,
        #     'varietal': varietal.xpath('text()').extract_first(),
        #     'location': location.xpath('text()').extract_first(),
        #     'price':price,
        #     'abv': abv,
        #     'RP': scores.get('RP',-1),
        #     'JS': scores.get('JS',-1),
        #     'WE': scores.get('WE',-1),
        #     'WS': scores.get('WS',-1),
        #     'V': scores.get('V',-1),
        # }




        # for plan in response.xpath('//body/div'):
        #     href = plan.css('a::attr(href)')[1]
        #     full_url = response.urljoin(href.extract())
        #     yield scrapy.Request(full_url, callback=self.parse_plan)

    # def parse_plan(self, response):
    #     # Extract phones available for plan
    #     phone_div = response.xpath('//div[@id="product-phones-list"]/div')
    #     phones = []
    #     for p in phone_div:
    #         phone = {
    #             'price': p.xpath('@data-price').extract()[0],
    #             'name': p.xpath('@data-name').extract()[0],
    #             'type': p.xpath('@data-type').extract()[0],
    #         }
    #         phones.append(phone)

    #     # Get name of plan
    #     name = ''
    #     if len(response.css('.col-xs-18 h1::text').extract()) != 0:
    #         name = response.css('.col-xs-18 h1::text').extract()[0]
    #     # Get name of provider
    #     provider = response.xpath('//strong/text()')[0].extract()
    #     #Extract things like data, price etc.
    #     attibutes = {}
    #     for attr in response.css('.col-xs-17').xpath('div'):
    #         if not attr.css('.col-sm-6') or not attr.css('.col-sm-18'):
    #             continue
    #         cat = attr.css('.col-sm-6')[0].xpath('strong/text()')[0].extract()
    #         if attr.css('.col-sm-18')[0].xpath('strong/text()'):
    #             value = attr.css('.col-sm-18')[0].xpath('strong/text()')[0].extract()
    #             attibutes[cat] = value
    #         elif attr.css('.col-sm-18')[0].xpath('span').extract():
    #             value = attr.css('.col-sm-18')[0].xpath('span').extract()[0]
    #             attibutes[cat] = value

        # Output results
        # yield {
        #     'url': response.url,
        #     'provider': provider,
        #     'plan_name': name,
        #     'minutes': attibutes.get('Minutes', ''),
        #     'text': attibutes.get('Messages', ''),
        #     'data': attibutes.get('Data', ''),
        #     'phones': phones,
        #     'price': attibutes.get('Total Price', ''),
        #     'contract': attibutes.get('Contract', ''),
        #     'deal': attibutes.get('Current Deal', ''),
        # }


# 'title': response.css('h1 a::text').extract()[0],
# 'votes': response.css('.question .vote-count-post::text').extract()[0],
# 'body': response.css('.question .post-text').extract()[0],
# 'tags': response.css('.question .post-tag::text').extract(),
# 'link': response.url,