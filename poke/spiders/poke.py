import scrapy


class PokeSpider(scrapy.Spider):
    name = 'poke'
    start_urls = ['https://pokemondb.net/pokedex/all']
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

    def start_requests(self):

        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.headers)
    def parse(self, response): 

        pokes = response.xpath('//*[@id="pokedex"]/tbody/tr')

        for poke in pokes:
            
            id = poke.xpath('td[1]/span[2]/text()').extract_first()
            name = poke.xpath('td[2]/a/text()').extract_first()
            alt_name = poke.xpath('td[2]/small/text()').extract_first()
            types  = poke.xpath('td[3]/a/text()').getall()
            
            yield {
                'id': id,
                'name': name,
                'alt_name': alt_name,
                'types': types 
            }


        
