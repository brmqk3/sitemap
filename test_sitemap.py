from bs4 import BeautifulSoup
import os
import unittest
from urllib_sitemap import get_images, get_links

class TestSitemap(unittest.TestCase):
    def setUp(self):
        if os.path.exists('test_sitemap.txt'):
            os.remove('test_sitemap.txt')
    
    def test_get_one_image_successful(self):
        # Finds the image url and adds it to the array
        img_text = '<img src="https://s17776.pcdn.co/wp-content/uploads/2016/05/adobe.png">'
        bs = BeautifulSoup(img_text)
        url = "http://example.com"
        all_images = []
        host_root = "example.com"
        image_array = get_images(bs, url, all_images, host_root, 'test_sitemap.txt')
        self.assertItemsEqual(image_array, ["https://s17776.pcdn.co/wp-content/uploads/2016/05/adobe.png"])
    
    def test_get_one_link_successful(self):
        # Finds the url and adds it to the array
        link_text = '<a href="https://example.com/who-we-are">Who we are</a>'
        bs = BeautifulSoup(link_text)
        url = "http://example.com"
        all_urls = []
        host_root = "example.com"
        link_array = get_links(bs, url, all_urls, host_root, 'test_sitemap.txt')
        self.assertItemsEqual(link_array, ["https://example.com/who-we-are"])
        
    
    def test_get_one_link_no_repeat_entry(self):
        # Will not add another array value for the same url
        link_text = '<a href="https://example.com/who-we-are">Who we are</a>'
        bs = BeautifulSoup(link_text)
        url = "http://example.com"
        all_urls = ["https://example.com/who-we-are"]
        host_root = "example.com"
        link_array = get_links(bs, url, all_urls, host_root, 'test_sitemap.txt')
        self.assertItemsEqual(link_array, [])
    