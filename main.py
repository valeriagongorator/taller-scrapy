import os
from scrapy.crawler import CrawlerProcess
from spiders.laptops_spider import LaptopsSpider
from spiders.books_spider import BooksSpider
from utils.transformers import process_laptops, process_books
from utils.database import init_db, save_data, run_queries

if __name__ == '__main__':
    os.makedirs('data', exist_ok=True)
    
    raw_laptops, raw_books = [], []

    process = CrawlerProcess(settings={'LOG_LEVEL': 'ERROR'})
    process.crawl(LaptopsSpider, data_list=raw_laptops)
    process.crawl(BooksSpider, data_list=raw_books)
    process.start()

    df_laptops = process_laptops(raw_laptops)
    df_books = process_books(raw_books)

    init_db()
    save_data(df_laptops, df_books)
    run_queries()