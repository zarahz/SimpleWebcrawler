# sources:
# - https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3
# - https://stackoverflow.com/a/38234394/8905485

import scrapy
import os

# enable scrapys' Spider functionalities
class UrlAndPasswordFinder(scrapy.Spider):
    # first define a name and the urls for the crawler
    name = "url_password_finder"
    start_urls = ['https://ubicomp.net/sw/task1.php']

    def checkForExistingFile(filename):
        # if a file with this name already exists delete it
        fileExists = os.path.isfile('./' + filename)
        if fileExists:
            os.remove('./' + filename)
            
    # define how the response should be parsed
    def parse(self, response):
       # setup a file in which the response is saved
       
       # the filename matches the character length of the response
       # if the content changes the length does too 
       # which results in a different filename
       filename = str(len(response.body)) + '.html'
       UrlAndPasswordFinder.checkForExistingFile(filename)
       
       with open(filename, 'wb') as f:
           # save the html body inside the file
           f.write(response.body)
            
# execution commands:
# get the content once: scrapy runspider scraper.py
# execute the crawler every X seconds: watch -n 100 scrapy runspider WebCrawler.py
  
  
