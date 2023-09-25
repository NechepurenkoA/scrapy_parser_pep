import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.css('#numerical-index a')
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        line = response.css('h1.page-title::text').get()
        splited_line = line.split('–')
        number = int(splited_line[0].strip().split()[1])
        name = splited_line[1].strip()
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        data = {
            'number': number,
            'name': name,
            'status': status
        }
        yield PepParseItem(data)
