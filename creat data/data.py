"""Created dataset from https://auto.ria.com/"""

import scrapy


class RiaSpider(scrapy.Spider):
	name = 'ria'
	start_urls = [f'https://auto.ria.com/uk/legkovie/?page=1{page}' for page in range(1,19000)]

	def start_requests(self):
		for url in self.start_urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		items = {}
		body = response.css('.paid')
		for item in body:
			items['title'] = item.css('.blue.bold::text').extract()[0]
			try:
				items['price$'] = item.css('.size22::text').extract()[0]
			except:
				items['price$'] = None 
			try:
				items['price'] = item.css('.i-block span::text').extract()[0]
			except:
				items['price'] = None 
			try:
				items['car_mileage'] = item.css('.item-char:nth-child(1)::text').extract()[0].split()[0]\
					 if item.css('.item-char:nth-child(1)::text').extract()[0].split()[0].isdigit()\
					 else 0
			except:
				items['car_mileage'] = None 
			try:
				tmp = item.css('.view-location+ .item-char::text').extract()[0].split(',')
				items['fuel'] = tmp[0]
				items['power'] = tmp[1].split()[0]
			except:
				items['fuel'] = None 
				items['power'] = None
			try:
				items['location'] = item.css('.view-location::text').extract()[0]
			except:
				items['location'] = None 
			try:
				items['transmission'] = item.css('.view-location~ .item-char+ .item-char::text').extract()[0]
			except:
				items['transmission'] = None 

			yield items