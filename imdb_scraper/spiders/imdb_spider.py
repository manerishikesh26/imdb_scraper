import json
import re
import scrapy

class IMDbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/chart/top']
    movie_json = []


    def parse(self, response):
        for index, li in enumerate(response.xpath('//*[@id="__next"]/main/div/div[3]/section/div/div[2]/div/ul/*')):
            if index == 50:
                break
            movie_name = li.xpath('.//h3[@class="ipc-title__text"]/text()').get()
            movie_name = re.sub(r'^\d+\.\s+', '', movie_name)
            movie_date = li.xpath('.//div[contains(@class, "feoqjK")]/span[@class="sc-b189961a-8 kLaxqf cli-title-metadata-item"][1]/text()').get()
            href_value = li.xpath('.//a[@class="ipc-title-link-wrapper"]/@href').get()
            movie_data = {'Movie': movie_name, 'Year': movie_date}
            yield scrapy.Request(response.urljoin(href_value), callback=self.parse_title, meta={'movie_data': movie_data})


    def parse_title(self, response):
        movie_data = response.meta.get('movie_data')
        base_xpath = '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[1]/section/div[2]/div/ul'
        
        director_names = []
        director_xpath_pattern = base_xpath + '/li[1]/div/ul/li[position()]/a/text()'
        director_elements = response.xpath(director_xpath_pattern)
        for director_element in director_elements:
            director_names.append(director_element.get())

        star_names = []
        stars_xpath_pattern = base_xpath + '/li[3]/div/ul/li[position()]/a/text()'
        star_elements = response.xpath(stars_xpath_pattern)
        for star_element in star_elements:
            star_names.append(star_element.get())
        
        movie_data['Director'] = director_names
        movie_data['Stars'] = star_names
        self.movie_json.append(movie_data)
        yield movie_data  # Yield the updated movie data object
        with open('new_output.json', 'w+', encoding='utf-8') as json_file:
            json.dump(self.movie_json, json_file, indent=4)
