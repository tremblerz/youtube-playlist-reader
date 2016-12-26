# -*- coding: utf-8 -*-
import scrapy
from youtube_playlist_reader.items import InfoSecUdacityItem
from selenium import webdriver
from selenium import common
from scrapy.selector import Selector
import time

class InfosecUdacitySpider(scrapy.Spider):
	name = "infosec-udacity"
	allowed_domains = ["youtube.com"]
	start_urls = ['https://www.youtube.com/playlist?list=PLAwxTw4SYaPkG-z00NybuIyDqT4sRh3ak']

	def __init__(self):
		self.driver = webdriver.Firefox()

	def parse(self, response):
		count = 3
		complete_page = False
		item = InfoSecUdacityItem()
		resp = self.driver.get(self.start_urls[0])
		more_button = self.driver.find_element_by_xpath('//button[contains(@class,"more-button")]')
		
		while complete_page != True:
			try:
				more_button.click()
				time.sleep(2)
				more_button = self.driver.find_element_by_xpath('//button[contains(@class,"more-button")]')
			except common.exceptions.NoSuchElementException:
				complete_page = True

		response = Selector(text = self.driver.page_source)
		titles = response.xpath('//tr[@class="pl-video yt-uix-tile "]/@data-title').extract()
		for number, title in enumerate(titles):
			item['filename'] = title
			item['number'] = number
			yield item