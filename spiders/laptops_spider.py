import scrapy

class LaptopsSpider(scrapy.Spider):
    name = 'laptops'
    start_urls = ['https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops']

    def __init__(self, data_list=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_list = data_list if data_list is not None else []

    def parse(self, response):
        for item in response.css('div.thumbnail'):
            self.data_list.append({
                'nombre': item.css('a.title::text').get(),
                'precio': item.css('h4.price::text').get(),
                'descripcion': item.css('p.description::text').get(),
                'calificacion': len(item.css('div.ratings span.glyphicon-star')),
                'url': response.urljoin(item.css('a.title::attr(href)').get())
            })