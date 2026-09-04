import scrapy

class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://books.toscrape.com/']

    def __init__(self, data_list=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_list = data_list if data_list is not None else []

    def parse(self, response):
        word_to_num = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
        for item in response.css('article.product_pod'):
            rating_class = item.css('p.star-rating::attr(class)').get().split()[-1]
            self.data_list.append({
                'nombre': item.css('h3 a::attr(title)').get(),
                'precio': item.css('p.price_color::text').get(),
                'calificacion': word_to_num.get(rating_class, 0),
                'disponibilidad': item.css('p.instock.availability::text').getall()[-1].strip(),
                'url': response.urljoin(item.css('h3 a::attr(href)').get()),
                'categoria': 'General'
            })