import scrapy

class QuotespiderSpider(scrapy.Spider):
    name = "quotespider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]
    quote_list = []  

    def parse(self, response):
        quotes = response.css('.quote')

        for quote in quotes:
            text = quote.css('.text::text').get()   
            yield {
                'quote': text,
            }    
            self.quote_list.append({'quote': text})  
        for element in self.quote_list:
            print(element)




