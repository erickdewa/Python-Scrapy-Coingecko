import scrapy

class JudulSpider(scrapy.Spider):
    name = 'judul'
    start_urls = []
    for i in range(1, 5):
        start_urls.append(f'https://www.coingecko.com/?locale=id&page={i}')

    def parse(self, response):
        # check url allowed
        # print(response.url)

        for i in response.css('tbody > tr'):
        # for i in response.css('table'):
            yield {
                'no': i.css('td.table-number::text').extract_first().replace('\n', ''),
                'name': i.css('td.coin-name div div:nth-child(2) div a:nth-child(1)::text').extract_first().replace('\n', ''),
                'tracker': i.css('td.coin-name div div:nth-child(2) div span::text').extract_first().replace('\n', ''),
                'img': i.css('td.coin-name div div:nth-child(1) img::attr(src)').extract_first(),
            }
