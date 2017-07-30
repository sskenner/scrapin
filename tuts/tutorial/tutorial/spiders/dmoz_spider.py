from scrapy.spider import BaseSpider

class DmozSpider(BaseSpider):
	name = "dmoz"
	allowed_domains = ["dmoztools.net"]
	start_urls = [
		"http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
		"http://dmoztools.net/Computers/Programming/Languages/Python/Resources/"
	]

	def parse(self, response):
		filename = response.url.split("/")[-2]
		open(filename, 'wb').write(response.body)

