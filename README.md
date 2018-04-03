# Sitemap

## Installation
1. Must have Python 2.7 installed
2. pip install bs4

## Execution of script
* Run "python urllib_sitemap.py --url=url_of_site_to_crawl"

## Execution of testing
* Run "python -m unittest test_sitemap"

## Reasoning
Based on the prompt, I decided that all was required was to crawl the page
and print out unique links in each page. I could very easily modify it to 
output every link from each page.

I decided not to do a more structured map for the entire heirarchy, just 
because that seemed like overkill. This would require a more significant 
amount of work.

At first, I was going to use the Scrapy module for Python. After some 
attempts, seemed like a little too complicated for what I was trying to do. 
Perhaps would use in the future if we wanted this to have more features.

## Future work
* Create a more structured sitemap, where the entire heirarchy is displayed.
* Could dockerize or create shell script to run in virtualenv, so no 
installation of modules is necessary
* Definitely would want to beef up the testing, currently only test basic functionality