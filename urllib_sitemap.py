import argparse
from bs4 import BeautifulSoup
import urllib2
import urlparse
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Gets the url to create a sitemap of.')
    parser.add_argument('--url', required=True, help='Initial url to create sitemap of')
    
    args = parser.parse_args()
    
    parsed = urlparse.urlparse(args.url)
    host_root = parsed.netloc
    # Will hold links to all images
    all_images = []
    # Will hold all urls
    all_urls = []
    all_urls.append(args.url)
    for url in all_urls:
        # Will hold only links found for the current url
        found_link_array = []
        # Will hold only images found for the current url
        found_img_array = []
        print "Parent Page: " + url

        try:
            bs = BeautifulSoup(urllib2.urlopen(url).read())
        except urllib2.HTTPError as e:
            print "Error: Failed to open " + url
            continue

        for link in bs.findAll('a', {'href':True}):
            abs_url = urlparse.urljoin(url, link['href'])
            parsed_url = urlparse.urlparse(abs_url)
            # Ensure it's not an external link, and that it's not just a section of a page we have already parsed
            if (parsed_url.netloc.endswith('.' + host_root) or parsed_url.netloc == host_root) and '#' not in abs_url:
                found_flag = False
                # Check through the current urls to ensure we don't have an exact match
                for existing_url in all_urls:
                    if existing_url == abs_url:
                        found_flag = True
                        break
                if not found_flag:
                    all_urls.append(abs_url)
                    found_link_array.append(abs_url)

        if found_link_array:
            print "Links:"
            for found in found_link_array:
                print "\t" + found
                    
        # Same process for images, except we won't be adding them to the list of urls
        for img in bs.findAll('img', {'src': True}):
            abs_url = urlparse.urljoin(url, img['src'])
            parsed_url = urlparse.urlparse(abs_url)
            if parsed_url.netloc.endswith('.' + host_root) or parsed_url.netloc == host_root:
                found_flag = False
                for existing_url in all_images:
                    if existing_url == abs_url:
                        found_flag = True
                        break
                if not found_flag:
                    all_images.append(abs_url)
                    found_img_array.append(abs_url)

        if found_img_array:
            print "Images:"
            for found in found_img_array:
                print "\t" + found