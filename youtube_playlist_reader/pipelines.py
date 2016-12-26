# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os, re
COURSE_VIDEOS = '/home/abhi/Downloads/CourseMaterial/Information_Security/GeorgiaTech/'

class YoutubePlaylistReaderPipeline(object):
	def process_item(self, item, spider):
		for old_filename in os.listdir(COURSE_VIDEOS):
			file_string = old_filename.split('-')
			if len(file_string) > 2:
				video_title = file_string[0]
				#print(video_title + "," + item['filename'])
				if video_title == item['filename']:
					filename = str(item['number']) + "-" + video_title
					os.rename(COURSE_VIDEOS + old_filename, COURSE_VIDEOS + filename)
					break
		return item