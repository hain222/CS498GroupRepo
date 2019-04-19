#!/usr/bin/env python3

# autotesting script
# contains tests for website link checking

# run with
# 'python3 webtest.py 2>/dev/null'

# T1 Tests album link
# T2 Tests artists link
# T3 Tests songs link

import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider(scrapy.Spider):
	handle_httpstatus_list = [404]
	name = 'isdbSpider'
	allowed_domains = ['128.163.232.191:8080']
	start_urls = [
		'http://128.163.232.191:8080/albums/',
		'http://128.163.232.191:8080/artists/',
		'http://128.163.232.191:8080/songs/',
	]

	def __init__(self, category=None):
		self.url_test_list = []

	def parse(self, response):
		if response.status == 404:
			print('FAILED')
		else:
			print('SUCCESS')

process = CrawlerProcess()
process.crawl(MySpider)
process.start()
