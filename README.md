# scrapy_dawnheadlines
Basic Scrapy Spider to scrape headlines from https://www.dawn.com

Notes:

- Using Scrapy version 1.4.0


- Command used to generate scrapy project: 
   
   $ scrapy startproject dawn
      

- Command used to generate basic scrapy spider:
    
   $ scrapy genspider basic www.dawn.com


- Run spider using command:
   
   $ scrapy crawl basic
      

- Run spider and save output as json file:
      
      $ scrapy crawl basic -o dawnheadlines.json

- Run spider and save output as jl file:
      
      $ scrapy crawl basic -o dawnheadlines.jl
      
- Programming notes:
  - modified items.py to add field required for scraping
  - modified basic.py spider, to add xpaths for scraping fields
