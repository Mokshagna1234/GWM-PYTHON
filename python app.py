import string
import random

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def generate_short_code(self):
        characters = string.ascii_letters + string.digits
        short_code = ''.join(random.choice(characters) for _ in range(6))
        return short_code

    def shorten_url(self, original_url):
        if not original_url:
            return 'Invalid request. Please provide a URL to shorten.'

        short_code = self.generate_short_code()
        self.url_map[short_code] = original_url

        short_url = 'http://entertainment.com/' + short_code  
        return short_url

    def redirect_to_original_url(self, short_code):
        original_url = self.url_map.get(short_code)

        if original_url:
            return original_url
        else:
            return 'URL not found.'

if __name__ == '__main__':
    url_shortener = URLShortener()

    
    original_url = "https://www.youtube.com/some/long/url"
    short_url = url_shortener.shorten_url(original_url)
    print("Shortened URL:", short_url)

    
    short_code = short_url.split('/')[-1]
    redirected_url = url_shortener.redirect_to_original_url(short_code)
    print("Redirected URL:", redirected_url)
